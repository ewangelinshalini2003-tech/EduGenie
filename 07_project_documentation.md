# Phase 7 — Project Documentation

## Overview

EduGenie is a local web-based learning assistant prototype. It offers topic explanations, question answering, study-material summaries, multiple-choice quizzes, and four-week learning plans.

## Setup and operation

- Requires Python 3 and a modern web browser.
- Optional live generation uses the `google-genai` package and `GEMINI_API_KEY` environment variable.
- Start with `python main.py` from the project directory and browse to `http://127.0.0.1:5001`.
- The app can produce demo responses without a key.

## API reference

Send JSON `POST` requests to the routes below. For example, `/api/explain` accepts `{"topic":"photosynthesis","level":"beginner"}`.

| Route | Required JSON fields |
|---|---|
| `/api/explain` | `topic`; optional `level` |
| `/api/ask` | `question` |
| `/api/summarize` | `content` |
| `/api/quiz` | `topic` |
| `/api/path` | `subject`, `goal` |

Successful responses contain a `result` string. Errors contain an `error` string. The server defaults to port `5001`; set `PORT` to use another port.

## Configuration and privacy

Store the Gemini key in an environment variable, never in Python, HTML, screenshots, or a public repository. Requests submitted in live mode are sent to the configured Gemini service. Avoid entering confidential, personal, or sensitive information. The current prototype does not include accounts or persistent user history.

## Known limitations

- Generated educational content may be incomplete or incorrect; verify important facts with trusted course materials.
- Demo fallbacks are examples and are not personalized or comprehensive.
- There is no database, user login, saved history, automated grading, or administrative interface.
- Testing status must be filled in after executing the test plan.
