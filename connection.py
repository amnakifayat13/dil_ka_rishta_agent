from agents import AsyncOpenAI , OpenAIChatCompletionsModel, RunConfig
import os
from dotenv import load_dotenv


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if gemini_api_key is None:
    raise ValueError("GEMINI_API_KEY is not set")

client = AsyncOpenAI(
    api_key=gemini_api_key,
      base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="gemini-2.0-flash"
)

config =RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

