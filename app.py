import streamlit as st

from rag import read_pdf
from agents import compare_resume_jd
from agents import interview_questions

st.set_page_config(page_title="Career Agent")

st.title("🤖 AI Career Mentor Agent")

resume_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

jd = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze"):

    if resume_file and jd:

        with st.spinner("Analyzing..."):

            resume_text = read_pdf(resume_file)

            analysis = compare_resume_jd(
                resume_text,
                jd
            )

            questions = interview_questions(jd)

        st.subheader("Analysis Report")
        st.write(analysis)

        st.subheader("Interview Questions")
        st.write(questions)

    else:
        st.warning(
            "Please upload resume and job description."
        )