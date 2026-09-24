"""Quiz-generation feature for EduGenie."""
from qna import generate_content


def generate_quiz(topic: str) -> str:
    prompt = f"""Create a 5-question multiple-choice quiz about {topic} for a college student.
Give four options (A-D) for each question. Put the answer key after a horizontal line.
Do not reveal answers beside questions."""
    fallback = f"""## {topic.title()} practice quiz

1. Which statement best describes {topic}?
   A. A basic definition  B. An unrelated idea  C. A random guess  D. A historical date
2. Why is {topic} important?
   A. It supports understanding  B. It has no use  C. It avoids practice  D. It replaces learning
3. What is a good way to study {topic}?
   A. Use examples  B. Skip revision  C. Memorize only headings  D. Ignore feedback
4. What should you do after learning a concept?
   A. Test yourself  B. Forget it  C. Change topic immediately  D. Avoid questions
5. What helps retention most?
   A. Spaced revision  B. One quick glance  C. No notes  D. Guessing

---
**Answer key:** 1-A, 2-A, 3-A, 4-A, 5-A"""
    return generate_content(prompt, fallback)
