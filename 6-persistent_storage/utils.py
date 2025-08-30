from google.genai import types
from google.adk.runners import Runner



async def call_agent_async(runner:Runner,user_id,session_id,query):
    """Call the agent asynchronously with user's query"""


    message = types.Content(role="user",parts=[types.Part(text=query)])


    for events in runner.run(
        user_id=user_id,
        session_id=session_id,
        new_message=message
    ):
        