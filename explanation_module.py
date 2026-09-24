"""Topic explanation feature for EduGenie."""
from qna import generate_content


def explain_topic(topic: str, level: str = "beginner") -> str:
    prompt = f"""Explain {topic} for a {level} learner.
Use simple language, a short real-world example, and 3 key takeaways.
Format the answer with headings and bullet points."""
    fallback = (
        f"## {topic.title()}\n\n{topic.title()} is a topic you can understand by breaking it into "
        "small ideas. Start with the definition, then connect it to an everyday example.\n\n"
        "### Key takeaways\n- Learn the basic meaning first.\n- Practice with one small example.\n"
        "- Review and explain it in your own words."
    )
    return generate_content(prompt, fallback)
