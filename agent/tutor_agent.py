from crewai import Agent, LLM

from config.settings import GROQ_API_KEY, MODEL_NAME
from tools.calculator_tool import calculator


def create_tutor_agent():
    llm = LLM(
        model=f"groq/{MODEL_NAME}",
        api_key=GROQ_API_KEY,
        temperature=0.3
    )

    tutor = Agent(
        role="Study Tutor",
        goal="""
        Help students understand academic topics clearly,
        step by step, according to their learning level.
        """,
        backstory="""
        You are a patient and supportive personal study tutor.

        Your job is to teach rather than simply give answers.
        Explain difficult concepts in simple language, use examples
        when helpful, and provide step-by-step solutions for problems.

        Always adapt your explanation to the student's level.
        If a calculation is required, use the Calculator tool.
        Encourage the student to understand the concept.
        """,
        tools=[calculator],
        llm=llm,
        memory=True,
        verbose=False,
        allow_delegation=False
    )

    return tutor
