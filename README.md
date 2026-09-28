from pathlib import Path

content = """# EduGenie – AI-Powered Learning Assistant

EduGenie is a web-based learning assistant designed to help students understand topics, revise study material, practise questions, and organize their learning. It brings several study-support tools together in one application.

## Table of Contents

- [Overview](#overview)
- [Objectives](#objectives)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation and Setup](#installation-and-setup)
- [Running the Application](#running-the-application)
- [Using EduGenie](#using-edugenie)
- [API Endpoints](#api-endpoints)
- [Gemini AI Configuration](#gemini-ai-configuration)
- [Testing](#testing)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [Project Phases](#project-phases)

## Overview

Students often need different kinds of academic support while studying: explanations of unfamiliar concepts, answers to questions, short revision notes, practice quizzes, and structured study plans. EduGenie is intended to make these activities accessible through a single, easy-to-use web application.

The application uses Python for its server-side functionality. When configured with a Gemini API key, it can request AI-generated learning content. If the key is not configured or the AI service is unavailable, the application can return predefined fallback responses for supported features.

## Objectives

- Provide students with simple explanations of academic topics.
- Offer concise guidance for study-related questions.
- Turn study material into revision-friendly summaries.
- Support self-assessment through multiple-choice quizzes.
- Help learners organize their goals with a structured study path.
- Keep the application modular so individual features can be maintained separately.

## Features

### 1. Explain a Topic
Accepts a topic and learner level. The explanation prompt asks for simple language, a real-world example, and three key takeaways.

### 2. Ask a Question
Accepts a student question and provides concise educational guidance, including an explanation of difficult terms and a revision tip.

### 3. Summarize Study Material
Accepts study text and produces a revision-oriented summary with a title, a short list of key points, and a final reminder.

### 4. Generate a Quiz
Creates a five-question multiple-choice quiz about a topic, with four options (A–D) for each question and an answer key.

### 5. Create a Learning Path
Creates a practical four-week learning plan for a subject and goal. The plan is organized around weekly focus areas, activities, and checkpoints.

## Technology Stack

- **Python** – application logic and server
- **Python standard library** – HTTP server, JSON handling, and request routing
- **Google Gemini API** – optional AI-generated responses
- **google-genai** – Python package used to connect to Gemini when enabled
- **HTML, CSS, and JavaScript** – browser-based user interface

## Project Structure

The project is organized into a server file and separate modules for the learning features.

```text
EduGenie/
├── main.py
├── qna.py
├── explanation_module.py
├── learning_path.py
├── quiz_module.py
├── summary_module.py
├── requirements.txt
├── .gitignore
└── templates/
    └── index.html

The exact interface-file location may differ in a modified version of the project. Keep the HTML file in the location expected by your main.py.

Main Files
File	Purpose
main.py	Starts the local web server and routes API requests to the appropriate feature.
qna.py	Handles Gemini communication, fallback responses, and question answering.
explanation_module.py	Builds the prompt and fallback response for topic explanations.
learning_path.py	Creates a four-week learning plan.
quiz_module.py	Creates a multiple-choice quiz.
summary_module.py	Summarizes study material for revision.
requirements.txt	Lists the optional Gemini package dependency.
templates/index.html	Contains the browser interface in versions that use a separate HTML template.
Requirements
Python 3.10 or later is recommended.
A modern web browser.
Internet access and a valid Gemini API key for live Gemini responses.
The google-genai package is needed only when using Gemini integration.

Check that Python is installed:

python --version
Installation and Setup
Download or clone the project.
Extract the project files, if downloaded as a ZIP.
Open a terminal or Command Prompt in the project folder.
(Optional) Install the dependency for Gemini integration:
python -m pip install -r requirements.txt

If you only want to use the application's fallback/demo responses, installing the Gemini package is not required.

Running the Application

From the project folder, run:

python main.py

The server's default local address is:

http://127.0.0.1:5001/

Open that address in your browser while the Python server is running. Keep the terminal window open during use. Press Ctrl+C in the terminal to stop the server.

If the page displays 404 – File not found, check that you are running the intended main.py and that the interface file exists at the path expected by that version of the server. Also check that you opened the correct local address and port.

Using EduGenie
Start the application.
Open the local address in your browser.
Select the learning tool you want to use.
Enter the required topic, question, study text, subject, or goal.
Submit the form and read the generated result.
Review the response and use it as a study aid alongside your class notes and textbooks.
API Endpoints

The Python server provides the following POST endpoints:

Endpoint	Purpose	Required input
/api/explain	Explain a topic	topic; optional level
/api/ask	Answer a study question	question
/api/summarize	Summarize study material	content
/api/quiz	Generate a quiz	topic
/api/path	Create a learning path	subject, goal

Requests use JSON, and successful responses return a result field. Error responses return an error field.

Gemini AI Configuration

Live AI responses are optional. To enable them, create a Gemini API key and set it as an environment variable named GEMINI_API_KEY.

Windows Command Prompt
set GEMINI_API_KEY=your_api_key_here
python main.py

This sets the key for the current Command Prompt session. Do not publish your API key, commit it to source control, or include it in screenshots or project documentation.

The application may also use the GEMINI_MODEL environment variable to select a model. If no key is configured, the project uses its fallback responses.

Testing

Test the application feature by feature:

Home page: confirm the web interface opens.
Topic explanation: submit a sample topic and learner level.
Question answering: submit a study-related question.
Summarization: paste a short paragraph and check the summary.
Quiz generation: submit a topic and check the questions and answer key.
Learning path: enter a subject and goal and check the four-week plan.
Fallback mode: run without GEMINI_API_KEY and confirm fallback content is returned.
Input validation: submit missing fields and confirm that an appropriate error is shown.

Record the expected result, actual result, and any issue found for each test.

Limitations
The quality and availability of live AI responses depend on the configured Gemini service and API key.
Fallback responses are predefined and may not be as specific as AI-generated responses.
The application is a learning aid; users should verify important academic information using trusted course materials.
The current project is a local application and does not include user accounts or persistent learning-history storage.
Future Enhancements
Add user registration and secure login.
Save summaries, quiz results, and learning plans.
Add progress tracking and personalized recommendations.
Improve the interface for mobile devices and accessibility.
Support file uploads for study material.
Add quiz scoring and performance reports.
Expand error handling, automated tests, and deployment options.
Project Phases

The project work can be documented in these eight phases:

Brainstorming and Ideation
Requirement Analysis
Project Design
Project Planning
Project Development
Project Testing
Project Documentation
Project Demonstration
Conclusion

EduGenie brings common study-support activities into one application. Its modular Python design separates the server from individual learning features, while optional Gemini integration enables AI-generated educational content. The project can be extended with additional learning tools, saved progress, and a more personalized student experience.
"""

path = Path("/mnt/data/README.md")
path.write_text(content, encoding="utf-8")
print(f"Created {path}")
