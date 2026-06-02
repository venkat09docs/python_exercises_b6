from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="You are expert in research on the AI concepts. with your experience explain the LLM concept as I am 10 years old"
)

print(response.output_text)