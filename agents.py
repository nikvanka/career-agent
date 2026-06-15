import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

def compare_resume_jd(resume, jd):

    prompt = f"""
    Compare this resume with the job description.

    Give:

    1. Matching Skills
    2. Missing Skills
    3. Resume Improvements
    4. Learning Roadmap

    Resume:
    {resume}

    Job Description:
    {jd}
    """

    response = llm.invoke(prompt)

    return response.content


def interview_questions(jd):

    prompt = f"""
    Generate:

    - Technical Questions
    - HR Questions
    - Scenario Based Questions

    For this job description:

    {jd}
    """

    response = llm.invoke(prompt)

    return response.content