"""Study material summarization feature."""
from qna import generate_content


def summarize_text(content: str) -> str:
    prompt = f"""Summarize the following study material for revision. Include a title, 5 or fewer bullets,
and a final 'Remember' line. Keep important definitions and facts.\n\n{content}"""
    sentences = [part.strip() for part in content.replace("\n", " ").split(".") if part.strip()]
    bullets = "\n".join(f"- {sentence}." for sentence in sentences[:5])
    fallback = f"## Quick revision summary\n\n{bullets or '- Review the supplied material carefully.'}\n\n**Remember:** revise the key terms, then test yourself without looking at notes."
    return generate_content(prompt, fallback)
