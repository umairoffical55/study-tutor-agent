import streamlit as st
from services.tutor_service import ask_tutor

st.set_page_config(
    page_title="Study Tutor Agent",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Study Tutor Agent")
st.write("Your personal AI tutor powered by CrewAI and Groq.")

st.sidebar.header("🎓 Student Settings")

subject = st.sidebar.selectbox(
    "Subject",
    [
        "General", "Mathematics", "Physics", "Chemistry",
        "Computer Science", "Python", "Artificial Intelligence", "Engineering"
    ]
)

level = st.sidebar.selectbox(
    "Student Level",
    ["Beginner", "Intermediate", "Advanced"]
)

mode = st.sidebar.selectbox(
    "Learning Mode",
    ["Explain", "Solve", "Practice"]
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask your Study Tutor...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Tutor is thinking..."):
            try:
                response = ask_tutor(
                    question=question,
                    subject=subject,
                    level=level,
                    mode=mode
                )

                st.markdown(response)

                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )

            except Exception as e:
                st.error("Something went wrong. Please check your configuration.")
                st.exception(e)
