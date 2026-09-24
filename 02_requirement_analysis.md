# Phase 2 — Requirement Analysis

## Functional requirements

| ID | Requirement | Acceptance condition |
|---|---|---|
| FR-01 | Show the EduGenie homepage at `/`. | The page loads from the local server without a 404. |
| FR-02 | Explain a topic for beginner, intermediate, or advanced learners. | A topic and level can be submitted; an explanation is shown. |
| FR-03 | Answer a student question. | A question can be submitted and a study response is shown. |
| FR-04 | Summarize study material. | Pasted content can be submitted and a revision summary is shown. |
| FR-05 | Generate a quiz. | A topic can be submitted and a five-question quiz with answer key is shown. |
| FR-06 | Create a learning path. | A subject and goal can be submitted and a four-week plan is shown. |
| FR-07 | Support demo operation without a Gemini key. | Each feature returns a fallback response when `GEMINI_API_KEY` is absent. |
| FR-08 | Support optional Gemini responses. | When configured, the server attempts to use the Gemini client. |
| FR-09 | Give users a useful error for missing input or failed requests. | Invalid requests receive an error response and the page displays a readable message. |

## Non-functional requirements

- **Usability:** forms use clear labels, examples, and visible status/results.
- **Compatibility:** use a modern browser and a supported Python environment.
- **Maintainability:** keep each study feature in its own Python module.
- **Configuration:** keep API credentials in environment variables, not source files.
- **Privacy:** the prototype does not promise persistent storage; avoid pasting sensitive personal information.
- **Reliability:** an unavailable Gemini service should fall back to a demo response.

## Constraints and assumptions

- The prototype runs locally on `127.0.0.1` and defaults to port `5001`.
- `google-genai` is optional for the fallback experience and required for live Gemini calls.
- Internet access and a valid API key are needed for live model responses.
- This describes prototype scope; performance, security, and accessibility still need evaluation.
