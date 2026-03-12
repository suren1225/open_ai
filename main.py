from openai import OpenAI
from agents.validator import create_prompt
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

spec_path = "specs/validation.yaml"

prompt = create_prompt(spec_path)

print("Generated Prompt:\n")
print(prompt)

response = client.responses.create(
    model="gpt-5-nano",
    input=prompt
)

print("\nAI Validation Result:\n")
print(response.output_text)