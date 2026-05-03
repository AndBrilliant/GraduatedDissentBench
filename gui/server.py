#!/usr/bin/env python3
"""
Graduated Dissent Bench — Local GUI Server
Serves on localhost only. Proxies API calls to OpenAI/DeepSeek/Anthropic.
Auto-loads API keys from ~/.keys/{openai,deepseek,anthropic}
Stores all runs as JSON in ./runs/

Usage:
    python server.py [--port 8000]
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

RUNS_DIR = Path(__file__).parent / "runs"
RUNS_DIR.mkdir(exist_ok=True)

KEYS_DIR = Path.home() / ".keys"

PROVIDERS = {
    "openai": {
        "url": "https://api.openai.com/v1/chat/completions",
        "models": ["gpt-5.4", "gpt-4.1", "o4-mini"],
    },
    "deepseek": {
        "url": "https://api.deepseek.com/chat/completions",
        "models": ["deepseek-chat", "deepseek-reasoner"],
    },
    "anthropic": {
        "url": "https://api.anthropic.com/v1/messages",
        "models": ["claude-opus-4-6", "claude-sonnet-4-6"],
    },
}

# ── Key loading ──────────────────────────────────────────────
SERVER_KEYS = {}  # provider -> key string


def load_keys():
    """Load API keys from ~/.keys/ at startup."""
    for provider in PROVIDERS:
        keyfile = KEYS_DIR / provider
        if keyfile.is_file():
            key = keyfile.read_text().strip()
            if key:
                SERVER_KEYS[provider] = key
                print(f"  Key loaded: {provider} ({keyfile})")
            else:
                print(f"  Key file empty: {keyfile}")
        else:
            print(f"  Key not found: {keyfile}")


def get_key(provider, client_key=None):
    """Return server-side key if available, otherwise fall back to client-provided key."""
    if provider in SERVER_KEYS:
        return SERVER_KEYS[provider]
    if client_key:
        return client_key
    return None


# ── Provider helpers ─────────────────────────────────────────

def model_to_provider(model_id):
    for provider, info in PROVIDERS.items():
        if model_id in info["models"]:
            return provider
    return None


def call_api(provider, model, prompt, api_key, max_tokens=4096):
    """Call an AI provider API. Returns dict with content, usage, timing."""
    start = time.time()

    if provider in ("openai", "deepseek"):
        url = PROVIDERS[provider]["url"]
        body = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
        }
        if provider == "openai":
            body["max_completion_tokens"] = max_tokens
        else:
            body["max_tokens"] = max_tokens

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }

    elif provider == "anthropic":
        url = PROVIDERS[provider]["url"]
        body = {
            "model": model,
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}],
        }
        headers = {
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        }
    else:
        raise ValueError(f"Unknown provider: {provider}")

    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            raw = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"API error {e.code}: {error_body}")

    elapsed_ms = (time.time() - start) * 1000

    # Extract content and usage
    if provider in ("openai", "deepseek"):
        content = raw["choices"][0]["message"]["content"]
        usage = {
            "input_tokens": raw.get("usage", {}).get("prompt_tokens", 0),
            "output_tokens": raw.get("usage", {}).get("completion_tokens", 0),
        }
    elif provider == "anthropic":
        content = raw["content"][0]["text"]
        usage = {
            "input_tokens": raw.get("usage", {}).get("input_tokens", 0),
            "output_tokens": raw.get("usage", {}).get("output_tokens", 0),
        }

    tokens_per_sec = 0
    if elapsed_ms > 0 and usage["output_tokens"] > 0:
        tokens_per_sec = round(usage["output_tokens"] / (elapsed_ms / 1000), 2)

    return {
        "content": content,
        "usage": usage,
        "duration_ms": round(elapsed_ms, 1),
        "tokens_per_second": tokens_per_sec,
        "model": model,
        "provider": provider,
        "raw_api_response": raw,
    }


# ── HTTP Handler ─────────────────────────────────────────────

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(Path(__file__).parent), **kwargs)

    def log_message(self, format, *args):
        sys.stderr.write(f"[server] {args[0]}\n")

    def do_POST(self):
        if self.path == "/api/call":
            self._handle_api_call()
        elif self.path == "/api/save":
            self._handle_save()
        else:
            self.send_error(404)

    def do_GET(self):
        if self.path == "/api/keys":
            self._handle_keys_status()
        elif self.path == "/api/demo-paper":
            self._handle_demo_paper()
        elif self.path == "/api/runs":
            self._handle_list_runs()
        elif self.path.startswith("/api/run/"):
            self._handle_get_run()
        elif self.path == "/" or self.path == "/index.html":
            self.path = "/index.html"
            super().do_GET()
        else:
            super().do_GET()

    def _read_body(self):
        length = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(length)) if length else {}

    def _json_response(self, data, status=200):
        body = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _handle_keys_status(self):
        """Tell the frontend which providers have server-side keys loaded."""
        self._json_response({
            "keys_dir": str(KEYS_DIR),
            "providers": {
                p: {
                    "loaded": p in SERVER_KEYS,
                    "hint": SERVER_KEYS[p][:8] + "..." if p in SERVER_KEYS else None,
                }
                for p in PROVIDERS
            }
        })

    def _handle_demo_paper(self):
        """Serve the anonymized test paper for the demo button."""
        demo_path = Path(__file__).parent / "test_paper_anon.txt"
        if not demo_path.exists():
            self._json_response({"error": "Demo paper not found"}, 404)
            return
        self._json_response({
            "paper_id": "TEST01",
            "text": demo_path.read_text(),
        })

    def _handle_api_call(self):
        try:
            req = self._read_body()
            model = req["model"]
            prompt = req["prompt"]
            client_key = req.get("api_key", "")
            max_tokens = req.get("max_tokens", 4096)

            provider = model_to_provider(model)
            if not provider:
                self._json_response({"error": f"Unknown model: {model}"}, 400)
                return

            # Use server-side key if available, fall back to client-provided
            api_key = get_key(provider, client_key)
            if not api_key:
                self._json_response({"error": f"No API key for {provider}. Add key to {KEYS_DIR / provider} or enter in the GUI."}, 400)
                return

            result = call_api(provider, model, prompt, api_key, max_tokens)
            self._json_response(result)

        except Exception as e:
            self._json_response({"error": str(e)}, 500)

    def _handle_save(self):
        try:
            data = self._read_body()
            run_id = data.get("run_id", f"run_{int(time.time())}")
            filename = f"{run_id}.json"
            filepath = RUNS_DIR / filename
            with open(filepath, "w") as f:
                json.dump(data, f, indent=2)
            self._json_response({"saved": filename, "path": str(filepath)})
        except Exception as e:
            self._json_response({"error": str(e)}, 500)

    def _handle_list_runs(self):
        runs = []
        for f in sorted(RUNS_DIR.glob("*.json"), key=os.path.getmtime, reverse=True):
            try:
                with open(f) as fh:
                    data = json.load(fh)
                runs.append({
                    "filename": f.name,
                    "run_id": data.get("run_id", f.stem),
                    "paper_id": data.get("paper_id", "?"),
                    "condition": data.get("condition", "?"),
                    "started_at": data.get("started_at", "?"),
                    "verdict": data.get("final_result", {}).get("verdict", "?"),
                })
            except Exception:
                runs.append({"filename": f.name, "run_id": f.stem, "error": "parse failed"})
        self._json_response(runs)

    def _handle_get_run(self):
        name = self.path.split("/api/run/", 1)[1]
        filepath = RUNS_DIR / name
        if not filepath.exists() or not filepath.is_file():
            self.send_error(404)
            return
        with open(filepath) as f:
            self._json_response(json.load(f))


def main():
    parser = argparse.ArgumentParser(description="Graduated Dissent Bench GUI Server")
    parser.add_argument("--port", type=int, default=8000, help="Port (default: 8000)")
    args = parser.parse_args()

    print(f"\n  Graduated Dissent Bench GUI")
    print(f"  Loading API keys from {KEYS_DIR}/...")
    load_keys()

    if not SERVER_KEYS:
        print(f"\n  WARNING: No keys found. Add key files to {KEYS_DIR}/")
        print(f"  Expected files: {KEYS_DIR}/openai, {KEYS_DIR}/deepseek, {KEYS_DIR}/anthropic")
        print(f"  You can still enter keys manually in the GUI.\n")
    else:
        print(f"  {len(SERVER_KEYS)}/3 providers configured\n")

    server = HTTPServer(("127.0.0.1", args.port), Handler)
    print(f"  http://localhost:{args.port}")
    print(f"  Runs stored in: {RUNS_DIR.resolve()}")
    print(f"  Press Ctrl+C to stop\n")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.server_close()


if __name__ == "__main__":
    main()
