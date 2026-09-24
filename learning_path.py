"""Personalized learning-path feature."""
from qna import generate_content


def create_learning_path(subject: str, goal: str) -> str:
    prompt = f"""Create a practical four-week learning path for {subject}. Student goal: {goal}.
For each week give the focus, two activities, and a checkpoint. Keep it realistic for a college student."""
    fallback = f"""## Four-week plan: {subject.title()}

**Goal:** {goal}

1. **Week 1 - Foundations:** learn core terms; make short notes. **Checkpoint:** explain two concepts aloud.
2. **Week 2 - Practice:** solve guided questions; review errors. **Checkpoint:** complete a small quiz.
3. **Week 3 - Application:** use concepts in examples or a mini-task. **Checkpoint:** submit or review one exercise.
4. **Week 4 - Revision:** revisit weak areas; take a timed self-test. **Checkpoint:** write an improvement plan."""
    return generate_content(prompt, fallback)
