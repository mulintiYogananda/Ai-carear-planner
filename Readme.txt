# 🚀 AI Career Roadmap Planner Agent

An intelligent AI-powered Career Mentor built using **Streamlit** and **Groq LLM API**.  
This agent analyzes user skills, education, strengths, weaknesses, and target career goals to generate a structured, personalized roadmap for success.

---

## 🎯 Project Overview

The AI Career Roadmap Planner Agent helps students and professionals:

- Perform skill gap analysis
- Generate phase-wise learning roadmaps
- Create weekly study plans
- Suggest practical projects
- Provide interview preparation strategies
- Improve resume quality
- Boost productivity, focus, and confidence

It acts as a **virtual AI career mentor**.

---

## 🧠 Tech Stack

- **Python**
- **Streamlit** (Frontend UI)
- **Groq API** (LLM - Llama 3.1 8B Instant)
- Session-based memory using Streamlit state

---

## 📌 Features

✅ Personalized Career Roadmap  
✅ Skill Gap Analysis  
✅ Structured Learning Phases  
✅ Weekly Study Planner  
✅ Project Recommendations  
✅ Interview Strategy Guidance  
✅ Resume Improvement Tips  
✅ Productivity & Focus Enhancement Advice  
✅ Download Roadmap as Text File  
✅ Follow-up Q&A Chat System  

---

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd <your-project-folder>
2️⃣ Install Dependencies
pip install streamlit groq
3️⃣ Add Your Groq API Key

Open the Python file and replace:

client = Groq(api_key="YOUR_GROQ_API_KEY")

⚠️ Important: Never upload your real API key to GitHub.

4️⃣ Run the Application
streamlit run career_planner.py

The app will open automatically in your browser.

📊 How It Works

User enters:

Education

Skills

Target Role

Time availability

Strengths & Weaknesses

The AI:

Analyzes skill gaps

Creates structured roadmap

Generates study plan

Suggests projects

Provides motivation & productivity tips

User can:

Download roadmap

Ask follow-up questions

🧩 Model Used

llama-3.1-8b-instant via Groq API

Optimized for:

Fast responses

Structured outputs

Low token cost