import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from backend.prompt_manager import MENTAL_HEALTH_PROMPT

load_dotenv()

class GeminiClient:
    def __init__(self):
        api_key = os.getenv("gemini_key")
        if not api_key:
            raise ValueError("gemini_key not found in environment variables")

        self.client = genai.Client(api_key=api_key)

        self.chat_session = self.client.chats.create(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=MENTAL_HEALTH_PROMPT,
                temperature=0.7
            )
        )

    def send_message(self, message: str):
        return self.chat_session.send_message(message)