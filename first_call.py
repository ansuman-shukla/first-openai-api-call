from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

user_prompt = input("Enter your prompt: ")

response = client.responses.create(
    model="gpt-4.1",
    input=[
        {"role": "user", "content": "You are a sarcastic Teacher AI.You will answer the user's questions in a sarcastic manner."},
        {
            "role": "user",
            "content": user_prompt
        }
    ]
)
print("Response from the AI:")
print(response.output_text)

print("\n" + "="*50)
print("TOKEN USAGE INFORMATION:")
print("="*50)
print(f"Input tokens: {response.usage.input_tokens}")
print(f"Input tokens details - Cached tokens: {response.usage.input_tokens_details.cached_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
print(f"Output tokens details - Reasoning tokens: {response.usage.output_tokens_details.reasoning_tokens}")
print(f"Total tokens: {response.usage.total_tokens}")
print("="*50)