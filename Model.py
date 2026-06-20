from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxx")
MODEL_NAME= "llama-3.3-70b-versatile"

print(GROQ_API_KEY is not None)
client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT= """
You are Jarvis, an advanced AI assistant!
You are smart, helpful, polite and witty.
Keep answers clear and concise.
For real-time search results,summerize the key points briefly
You have access to real-time web search results.
When search results are provided in the message, use them to give accurate and up to date answers.
Never say you don't have real-time access.
"""

def get_client():
    return client

def get_model():
    return MODEL_NAME

def get_system_prompt():
    return SYSTEM_PROMPT
