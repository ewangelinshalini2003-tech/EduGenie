# Phase 8 — Project Demonstration

## Demonstration goal

Show that a student can open EduGenie and use its five study tools. The demo can run without a Gemini key using fallback responses; explain that live answers require a separately configured key.

## Preparation

1. Start the server from the project directory with `python main.py`.
2. Open `http://127.0.0.1:5001` in a browser.
3. Use non-sensitive sample content. Do not display API keys or private information.
4. Confirm the server is running and the homepage loads before recording or presenting.

## Suggested walkthrough

1. **Introduction:** “EduGenie brings common study tasks into one simple interface.”
2. **Explain:** select “Explain a topic,” enter `photosynthesis`, choose “Beginner,” and generate an explanation.
3. **Ask:** enter “Why do seasons change?” and show the response and revision tip.
4. **Summarize:** paste a short, non-sensitive paragraph and generate a revision summary.
5. **Quiz:** request a quiz on `cell biology` and point out the questions and answer key.
6. **Learning plan:** enter `Python programming` and a goal such as “write a small command-line program,” then show the four-week plan.
7. **Close:** explain the demo fallback and optional Gemini setup for live generation.

## Expected observations

- The home page is available at the local URL.
- Each tool presents the right input fields and returns a visible response or readable error.
- No API key is required to demonstrate fallback behavior.

## Presenter notes

Replace sample prompts with course-appropriate examples if needed. Report only results observed during the actual demonstration. If a live provider is unavailable, continue in demo mode and disclose that the live integration was not demonstrated.
