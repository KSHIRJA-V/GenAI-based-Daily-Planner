import streamlit as st
from planner import generate_schedule
from dotenv import load_dotenv

load_dotenv() 
import os

st.set_page_config(page_title="AI Daily Planner", layout="centered")
st.title(" AI Based Daily Schedule Maker!")


api_key = os.getenv("GEMINI_API_KEY")

goals = st.text_area("What are your goals for today?", height=150)
hours = st.slider("Working hours available today", min_value=2, max_value=16, value=8)

if st.button("Generate Schedule"):
    if not api_key or not goals.strip():
        st.error("Missing API key or goals.")
    else:
        with st.spinner("Generating your schedule..."):
            result = generate_schedule(goals, hours)
            st.success("Here's your plan:")
            st.markdown(f"```markdown\n{result}\n```")
