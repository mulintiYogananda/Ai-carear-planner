import streamlit as st
from groq import Groq

# ==============================
# 🔑 GROQ API KEY
# ==============================
client = Groq(api_key="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")
# ==============================
# 🎨 PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Career Roadmap Planner Agent",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Career Roadmap Planner Agent")
st.markdown("Your Personal AI Career Mentor")

# ==============================
# 🧠 SESSION MEMORY
# ==============================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ==============================
# 📋 USER INPUT FORM
# ==============================
with st.form("career_form"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Your Name")
        current_education = st.text_input("Current Education (e.g., 3rd Year B.Tech CSE-AI)")
        current_skills = st.text_area("Current Skills")
        target_role = st.text_input("Target Role (e.g., ML Engineer, Data Scientist)")

    with col2:
        time_available = st.selectbox(
            "Time Available to Prepare",
            ["3 Months", "6 Months", "1 Year", "More than 1 Year"]
        )
        daily_hours = st.selectbox(
            "Daily Study Time",
            ["1-2 Hours", "3-4 Hours", "5+ Hours"]
        )
        strengths = st.text_area("Your Strengths")
        weaknesses = st.text_area("Your Weaknesses")

    submitted = st.form_submit_button("Generate Career Roadmap")

# ==============================
# 🧠 AI GENERATION
# ==============================
if submitted:
    with st.spinner("Generating your personalized roadmap..."):

        prompt = f"""
        You are a professional AI Career Mentor Agent.

        Create a structured, step-by-step career roadmap.

        Candidate Details:
        Name: {name}
        Education: {current_education}
        Current Skills: {current_skills}
        Target Role: {target_role}
        Time Available: {time_available}
        Daily Study Time: {daily_hours}
        Strengths: {strengths}
        Weaknesses: {weaknesses}

        Provide:
        1. Skill Gap Analysis
        2. Phase-wise Roadmap (with timeline)
        3. Weekly Study Plan
        4. Project Suggestions
        5. Interview Preparation Strategy
        6. Resume Improvement Tips
       7.Irrespective of all the student details, help him by giving the guidence
        being concistence,focus and starting new habits .give some tips increase his study productivity
        make him feel confidence and better.Give all tips 
        Keep it structured and clear.
        """

        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an expert AI career planning assistant."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant"
        )

        roadmap = response.choices[0].message.content

        st.session_state.chat_history.append(roadmap)

# ==============================
# 📊 DISPLAY OUTPUT
# ==============================
if st.session_state.chat_history:
    st.markdown("## 📌 Your Personalized Career Roadmap")
    st.write(st.session_state.chat_history[-1])

    st.download_button(
        label="📥 Download Roadmap as Text",
        data=st.session_state.chat_history[-1],
        file_name="career_roadmap.txt"
    )

# ==============================
# 💬 FOLLOW-UP CHAT SECTION
# ==============================
st.markdown("---")
st.subheader("💬 Ask Follow-up Questions")

user_question = st.text_input("Ask anything about your roadmap...")

if st.button("Ask"):
    if user_question:
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are an AI Career Mentor helping refine the roadmap."},
                    {"role": "user", "content": user_question}
                ],
                model="llama-3.1-8b-instant"
            )

            answer = response.choices[0].message.content
            st.write(answer)