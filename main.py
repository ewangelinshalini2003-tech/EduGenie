"""EduGenie - a Gemini-powered learning assistant web application."""
import json
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from explanation_module import explain_topic
from learning_path import create_learning_path
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text

ROOT = Path(__file__).resolve().parent


class EduGenieHandler(SimpleHTTPRequestHandler):
    """Serve the web page and the five learning-tool endpoints."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return
        if path == "/":
            self.path = "/templates/index.html"
        return super().do_GET()

    def do_POST(self):
        routes = {
            "/api/explain": lambda d: explain_topic(d["topic"], d.get("level", "beginner")),
            "/api/ask": lambda d: answer_question(d["question"]),
            "/api/summarize": lambda d: summarize_text(d["content"]),
            "/api/quiz": lambda d: generate_quiz(d["topic"]),
            "/api/path": lambda d: create_learning_path(d["subject"], d["goal"]),
        }
        try:
            data = json.loads(self.rfile.read(int(self.headers.get("Content-Length", "0"))) or b"{}")
            route = routes.get(urlparse(self.path).path)
            if not route:
                raise KeyError("unknown feature")
            result = route({key: str(value).strip() for key, value in data.items()})
            self._send_json(200, {"result": result})
        except (KeyError, ValueError) as error:
            self._send_json(400, {"error": f"Please complete the required fields ({error})."})
        except Exception:
            self._send_json(500, {"error": "EduGenie could not process that request. Please try again."})

    def _send_json(self, status, body):
        payload = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5001"))
    server = ThreadingHTTPServer(("127.0.0.1", port), EduGenieHandler)
    print(f"EduGenie is running at http://127.0.0.1:{port}")
    server.serve_forever()
