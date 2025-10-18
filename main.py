from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
import chainlit as cl
import os
from dotenv import load_dotenv

load_dotenv()

model = OpenAIChatModel(
    'google/gemini-2.5-flash-lite',
    provider=OpenAIProvider(
        base_url='https://openrouter.ai/api/v1',
        api_key=os.getenv("OPENROUTER_API_KEY"),
    ),
)

simple_agent = Agent(
    model=model,
    system_prompt=(
        'Please answer everything in hong kong traditional chinese'
    ),
)

@cl.on_chat_start
def on_start():
    cl.user_session.set("agent", simple_agent)

@cl.on_message
async def on_message(message: cl.Message):
    agent = cl.user_session.get("agent")
    response = agent.run_sync(message.content)
    await cl.Message(content=response.output).send()