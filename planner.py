import os
from dotenv import load_dotenv
import google.generativeai as genai



load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


model = genai.GenerativeModel("models/gemini-1.5-flash")



def generate_schedule(goals, hours_per_day=8):
    prompt = f"""
You are a smart daily planner. Given the following goals:

{goals}

Create a structured plan for the day assuming {hours_per_day} working hours. Include breaks and use this format:

Time | Task
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Gemini API Error: {e}"
