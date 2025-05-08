import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_assistant_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an L1 IT Helpdesk assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]