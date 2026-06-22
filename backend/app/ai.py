import random

def generate_ai_insights(title: str, description: str) -> dict:
    """
    Simulates an AI processing the task text to give time estimates and study tips.
    Later, we can plug a real LLM API here!
    """
    text = (title + " " + (description or "")).lower()
    
    # Simple keyword-based rules to simulate "smart" responses
    if "math" in text or "calculus" in text:
        estimate = "2.5 Hours"
        tip = "Practice active recall. Do 3 practice problems without looking at the solutions."
    elif "code" in text or "programming" in text or "docker" in text:
        estimate = "3 Hours"
        tip = "Break the coding session into 25-minute Pomodoro blocks. Write the code manually instead of copying."
    elif "read" in text or "history" in text or "chapters" in text:
        estimate = "1.5 Hours"
        tip = "Summarize each section in your own words after reading instead of highlighting lines."
    else:
        estimate = "1 Hour"
        tip = "Stay focused! Clear all distractions and keep a water bottle nearby."
        
    return {
        "ai_time_estimate": estimate,
        "ai_study_tip": tip
    }
