from crewai import Task


def create_tutor_task(agent, question, subject, level, mode):
    return Task(
        description=f"""
        Help the student with this request.

        Subject: {subject}
        Student Level: {level}
        Learning Mode: {mode}
        Student Question: {question}

        Instructions:
        1. Understand what the student is asking.
        2. Adapt the explanation to the student's level.
        3. Explain the concept clearly.
        4. Use a simple example when useful.
        5. If it is a problem-solving question, solve it step by step.
        6. Use the Calculator tool when mathematical calculations are required.
        7. Do not make the answer unnecessarily complicated.
        8. Encourage learning rather than simply giving an answer.
        9. If appropriate, finish with a short practice question.

        Give a helpful response directly to the student.
        """,
        expected_output="""
        A clear tutor response containing an explanation,
        example or steps when appropriate, and the final answer when required.
        """,
        agent=agent
    )
