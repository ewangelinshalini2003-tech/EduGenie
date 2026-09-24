# Phase 3 — Project Design

## Architecture

```text
Browser (templates/index.html)
        │ HTTP GET / and POST /api/*
        ▼
Python HTTP server (main.py)
        │ dispatches by API route
        ├── explanation_module.py
        ├── qna.py (question answering and shared Gemini integration)
        ├── summary_module.py
        ├── quiz_module.py
        └── learning_path.py
```

The server serves the homepage and static project files. Each POST endpoint accepts JSON, calls its feature function, and returns a JSON result. Feature modules provide a demo fallback; `qna.py` optionally calls Gemini using environment configuration.

## API design

| Method and path | Input fields | Purpose |
|---|---|---|
| `GET /` | — | Serve the EduGenie homepage. |
| `POST /api/explain` | `topic`, optional `level` | Explain a topic for a learner level. |
| `POST /api/ask` | `question` | Answer a student question. |
| `POST /api/summarize` | `content` | Summarize pasted material. |
| `POST /api/quiz` | `topic` | Generate a practice quiz. |
| `POST /api/path` | `subject`, `goal` | Generate a four-week learning path. |
| `GET /favicon.ico` | — | Return an empty response when no icon is provided. |

Successful API responses use `{"result": "..."}`. Input/route errors use HTTP 400 and an `error` field; unexpected processing errors use HTTP 500.

## Interface design

The homepage presents the five study tools in a compact navigation area. Selecting a tool displays its input form. Submitting shows progress, then the result or an error message. Layout adapts for smaller screens.

## Design decisions

- Use Python's standard-library HTTP server to keep the prototype easy to run.
- Separate feature logic into modules to make later changes easier.
- Keep the interface as a static HTML page with browser-side JavaScript.
- Treat model responses as text in the interface rather than interpreting returned markup as trusted HTML.
