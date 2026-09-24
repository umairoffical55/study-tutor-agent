from crewai import Crew, Process

from agent.tutor_agent import create_tutor_agent
from agent.tutor_task import create_tutor_task


def ask_tutor(question, subject, level, mode):
    tutor = create_tutor_agent()

    task = create_tutor_task(
        agent=tutor,
        question=question,
        subject=subject,
        level=level,
        mode=mode
    )

    crew = Crew(
        agents=[tutor],
        tasks=[task],
        process=Process.sequential,
        memory=True,
        verbose=False
    )

    result = crew.kickoff()
    return result.raw
