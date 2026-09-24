"""Gemini connection and question-answer feature.

Set GEMINI_API_KEY in your environment to enable live AI answers. Without a key,
EduGenie uses safe, presentation-friendly fallback responses.
"""
import os


def generate_content(prompt: str, fallback: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return fallback + "\n\n*Demo mode: add GEMINI_API_KEY for a live Gemini response.*"

    try:
        from google import genai

        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"), contents=prompt
        )
        return response.text or fallback
    except Exception as error:
        return fallback + f"\n\n*Gemini was unavailable ({error.__class__.__name__}); showing demo response.*"


def answer_question(question: str) -> str:
    prompt = f"""You are EduGenie, a supportive learning assistant. Answer this student question:
{question}

Be accurate, concise, and educational. Explain any difficult term. End with one quick revision tip."""
    fallback = (
        "## Study guidance\n\nStart by identifying the main concept in your question and write its "
        "definition in one sentence. Then find one worked example from your notes or textbook.\n\n"
        "**Revision tip:** use the 'explain it aloud' method - teach the idea in your own words."
    )
    return generate_content(prompt, fallback)
