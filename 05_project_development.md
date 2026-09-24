# Phase 5 — Project Development

## Implemented structure

```text
EDUCATION AI/
├── main.py
├── explanation_module.py
├── learning_path.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── requirements.txt
├── templates/
│   └── index.html
└── project_docs/
    ├── 01_brainstorming_ideation.md
    ├── 02_requirement_analysis.md
    ├── 03_project_design.md
    ├── 04_project_planning.md
    ├── 05_project_development.md
    ├── 06_project_testing.md
    ├── 07_project_documentation.md
    └── 08_project_demonstration.md
```

## Main implementation

- `main.py` runs a threaded local HTTP server, serves the homepage, and dispatches the five JSON API routes.
- `explanation_module.py` builds topic explanations at a selected level.
- `qna.py` answers questions and provides shared Gemini integration with demo fallback behavior.
- `summary_module.py` creates a short revision summary.
- `quiz_module.py` creates a five-question practice quiz.
- `learning_path.py` creates a four-week plan.
- `templates/index.html` provides the browser interface, forms, request handling, and response display.
- `requirements.txt` lists the optional Gemini client dependency.

## Run locally

1. Install Python 3.
2. In a terminal, change to the project directory.
3. Optionally install dependencies with `python -m pip install -r requirements.txt`.
4. Optionally set `GEMINI_API_KEY` in the environment for live model responses. Do not commit the key.
5. Start the app with `python main.py`.
6. Open `http://127.0.0.1:5001` in a browser.

Without a Gemini key, the feature modules return demo responses. Stop the server with Ctrl+C in its terminal.
