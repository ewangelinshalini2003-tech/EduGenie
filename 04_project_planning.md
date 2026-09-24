# Phase 4 — Project Planning

## Work plan

| Work package | Planned work | Completion evidence |
|---|---|---|
| 1. Define the problem | Identify student study needs and choose a focused prototype. | Brainstorming and requirement documents. |
| 2. Design the solution | Define modules, routes, request fields, and user flow. | Architecture and API design. |
| 3. Build the server | Implement homepage serving, API dispatch, and JSON responses. | `main.py`. |
| 4. Build study features | Implement explanation, Q&A, summary, quiz, and learning-path modules. | Feature modules. |
| 5. Build the interface | Create input forms and result/error display for each feature. | `templates/index.html`. |
| 6. Verify behavior | Check startup, routes, validation, fallback mode, and configured live mode. | Completed test record. |
| 7. Prepare submission | Add project documentation and demo materials; publish a public repository if required. | Repository link and phase documents. |

## Dependencies and resources

- Python 3 and a browser.
- Optional `google-genai` package and Gemini API key for live responses.
- Local machine for development and demonstration.
- Git and a public GitHub repository for submission, if required by the course.

## Risks and responses

- **Missing page or asset:** check paths and confirm homepage files are included in version control.
- **Missing API key or network:** demonstrate fallback mode and explain that live generation is optional.
- **Model response failure:** show a fallback response and avoid losing the user's form input.
- **Unverified quality:** record actual results during testing; do not present planned checks as completed tests.
- **Public repository exposure:** review files for API keys and personal data before publishing.

## Status

The prototype files and homepage are present. The test plan and demonstration guide are prepared in companion phase documents. Record test results and repository details when those activities are completed.
