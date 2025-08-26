import uuid
import asyncio

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from faq_agent import faq_agent

load_dotenv()

stateful_session_service = InMemorySessionService()

_initial_state_ = {
    "user_name": "Thanos",
    "user_prefernces": """
    I don't have a beard.
    I am like an orc, not green but purple.
    I like to snap my fingers which gives the sound 'snap' and I call this 'The Snap'.
    After I do the snap I like to rest and watch the sunrise on a grateful universe.
    My favourite quote is 'vinil ayya nisa api goda giya malli'.
    I have a gaunlet in my right hand that have six slots embedded with the six infinity stones.
    The stones are bought from 'vinil ayya'.
    My favourite movie series is John Wick.
    My favourite hero is 'Mahaurga dawanthaya'
    """
}

APP_NAME = "Thanos Bot"
USER_ID = "thanos"
SESSION_ID = str(uuid.uuid4())

async def main():
    print("creating session")
    stateful_session = await stateful_session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state=_initial_state_,
        session_id=SESSION_ID
    )

    print("Created Session")
    print(f"\t Session ID: {SESSION_ID}")

    runner = Runner(
        app_name=APP_NAME,
        agent=faq_agent,
        session_service=stateful_session_service
    )

    new_message = types.Content(
        role="user", parts=[types.Part(text="can you tell me about thanos in one sentence?")],
    )

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print(f"Question: {new_message.parts[0].text}")
                print(f"Final response: {event.content.parts[0].text}")

    print("==== Session Event Exploration ====")
    session = await stateful_session_service.get_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )

    print("=== Final Session State ===")
    for key, value in session.state.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    asyncio.run(main())