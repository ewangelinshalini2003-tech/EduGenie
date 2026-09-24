# Phase 6 — Project Testing

## Test plan

Record the date, environment, actual result, and pass/fail outcome when each check is run. These are test cases, not a claim that the checks have already been executed.

| ID | Check | Expected result | Actual result / status |
|---|---|---|---|
| TC-01 | Start the application using the documented command. | Server starts and prints its local URL. | Not recorded |
| TC-02 | Open `/` in a browser. | EduGenie homepage loads; no homepage 404. | Not recorded |
| TC-03 | Request `/favicon.ico`. | No missing-file 404 (empty response is acceptable). | Not recorded |
| TC-04 | Submit each of the five forms with valid sample input and no API key. | Each endpoint returns a demo result. | Not recorded |
| TC-05 | Submit a request with a required field omitted. | A readable validation/error response is shown. | Not recorded |
| TC-06 | Send a request to an unknown API path. | Server returns a client error response. | Not recorded |
| TC-07 | Configure a valid Gemini key and submit a prompt. | Live response is returned, or a fallback appears if the provider fails. | Not recorded |
| TC-08 | Use the page at a narrow viewport. | Navigation and forms remain usable without horizontal overflow. | Not recorded |

## Reporting defects

For each defect, record the test ID, reproduction steps, input used (excluding secrets), expected result, actual result, and relevant server/browser error. Never include an API key in screenshots or reports.

## Test summary

**Execution status:** pending. Populate the result column after running the test plan and include fixes and retest outcomes before submitting the testing phase.
