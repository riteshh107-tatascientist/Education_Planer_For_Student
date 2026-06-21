import streamlit as st
import google.generativeai as genai
from datetime import date
import os
from dotenv import load_dotenv

# Load environmental variables securely from .env file
load_dotenv()

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="SmartStudy AI",
    page_icon="📚",
    layout="wide"
)

# =========================
# MODERN UI / NEON-GLASSMORPHISM CUSTOM CSS
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

/* Global Styles */
.main {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
    color: #f8fafc;
    font-family: 'Poppins', sans-serif;
}

/* Headings */
.big-title {
    text-align: center;
    font-size: 45px;
    font-weight: 700;
    background: linear-gradient(45deg, #38bdf8, #818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 20px;
    margin-bottom: 5px;
    animation: fadeInDown 1s ease-out;
}

.tagline {
    text-align: center;
    font-size: 18px;
    color: #94a3b8;
    margin-bottom: 30px;
    animation: fadeInUp 1.2s ease-out;
}

/* Glassmorphism Feature Boxes with Animations */
.feature-box {
    background: rgba(30, 41, 59, 0.45);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    padding: 25px;
    border-radius: 16px;
    margin: 15px 0;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    animation: fadeInUp 1s ease-out;
}

/* Box Hover Effect */
.feature-box:hover {
    transform: translateY(-10px);
    border-color: #38bdf8;
    box-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
    background: rgba(30, 41, 59, 0.65);
}

.feature-box h3 {
    color: #38bdf8;
    margin-top: 0;
    font-weight: 600;
}

/* Marquee Header styling */
.marquee {
    width: 100%;
    overflow: hidden;
    white-space: nowrap;
    box-sizing: border-box;
    background: rgba(15, 23, 42, 0.8);
    border-bottom: 2px solid #38bdf8;
    padding: 10px 0;
}

.marquee span {
    display: inline-block;
    padding-left: 100%;
    animation: marquee 20s linear infinite;
    font-size: 16px;
    color: #facc15;
    font-weight: 600;
    letter-spacing: 1px;
}

/* Keyframe Animations */
@keyframes marquee {
    0% { transform: translateX(0); }
    100% { transform: translateX(-100%); }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Footer styling */
.footer {
    text-align: center;
    margin-top: 60px;
    padding: 25px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(15, 23, 42, 0.6);
    border-radius: 12px;
}

.footer h4 {
    color: #818cf8;
    margin-bottom: 15px;
}

.footer a {
    color: #38bdf8;
    text-decoration: none;
    margin: 0 10px;
    font-weight: 500;
}

.footer a:hover {
    color: #facc15;
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# =========================
# MOVING HEADER (Branding Update)
# =========================
st.markdown("""
<div class='marquee'>
<span>
🚀 ELEVATE 2026 HACKATHON | NOIDA INSTITUTE OF ENGINEERING & TECHNOLOGY | 
TECHNOCRATS INSTITUTE OF TECHNOLOGY (TIT), BHOPAL | SMARTSTUDY AI BY RITESH KUMAR SINGH
</span>
</div>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='big-title'>📚 SmartStudy AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='tagline'>Turn Exam Stress Into Smart Success</div>",
    unsafe_allow_html=True
)

st.write("")

# =========================
# SIDEBAR SECURE STATUS
# =========================
st.sidebar.title("⚙️ SmartStudy AI")

# Safely extract key from the .env environment setup
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    st.sidebar.success("🔒 API Key Loaded Securely!")
else:
    st.sidebar.error("❌ API Key Missing in .env file")

st.sidebar.info("Institution:\nTechnocrats Institute of Technology, Bhopal")
st.sidebar.info("Personalized schedules for every student.")

# =========================
# HOME SECTION WITH ANIMATED CARDS
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='feature-box'>
    <h3>🎯 Personalized Plans</h3>
    Study plans uniquely engineered and tailored to your core college subjects.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='feature-box'>
    <h3>⚡ AI Powered</h3>
    Leverages Gemini LLMs to generate smart, balanced schedules instantly.
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='feature-box'>
    <h3>📈 Peak Performance</h3>
    Designed to maximize your focus parameters and optimize exam outputs.
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# USER INPUT
# =========================
st.subheader("📝 Create Your Study Plan")

name = st.text_input("Student Name", value="Ritesh Kumar Singh")

subjects = st.text_area(
    "Subjects (comma separated)",
    placeholder="Data Science, Machine Learning, MySQL, Python, Mathematics"
)

hours = st.slider(
    "Study Hours Per Day",
    1,
    12,
    5
)

exam_date = st.date_input(
    "Exam Date",
    min_value=date.today()
)

# =========================
# GENERATE PLAN
# =========================
if st.button("🚀 Generate Study Plan"):

    if not api_key:
        st.error("Cannot run query: Please update your hidden `.env` file with a valid Gemini API Key.")
    else:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-3.5-flash")

        prompt = f"""
        Student Name: {name}
        Institution: Technocrats Institute of Technology (TIT), Bhopal
        Subjects: {subjects}
        Available Study Hours Per Day: {hours}
        Exam Date: {exam_date}

        Create:
        1. Daily Study Plan
        2. Subject Priority (Give more weightage to critical Data Science/Programming domains if applicable)
        3. Weekly Schedule
        4. Revision Strategy
        5. Motivation Tips for Hackathon/Engineering students

        Format professionally and neatly using Markdown.
        """

        with st.spinner("Analyzing parameters and generating AI Study Plan..."):
            try:
                response = model.generate_content(prompt)
                st.success("Plan Generated Successfully!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred while generating: {e}")

# =========================
# FOOTER (Branding Update)
# =========================
st.markdown("""
<div class='footer'>
<h4>Developed By Ritesh Kumar Singh</h4>
<p style='color: #94a3b8;'>Technocrats Institute of Technology (TIT), Bhopal</p>
<a href="https://www.linkedin.com/in/ritesh-kumar-singh-a91866402/" target="_blank">🔗 LinkedIn</a> | 
<a href="https://github.com/riteshh107-tatascientist" target="_blank">💻 GitHub</a>
<br><br>
<span style='color: #64748b; font-size: 13px;'>ELEVATE 2026 Hackathon Submission</span>
</div>
""", unsafe_allow_html=True)