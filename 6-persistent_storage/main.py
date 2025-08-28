import asyncio

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from memory_agent import memory_agent




load_dotenv

#================== Part 1 - Intialize Persistant Session Service
db_url = "sqlite:///./my_agent_data.db"
database_session_service = DatabaseSessionService(db_url=db_url)


#================== Part 2 - Define inital state
_initial_state_ = {
    "name":"Thanos",
    "reminder":[]
}


async def main_async():
    # Setup constraints
    APP_NAME="Memory agent"
    USER_ID="Thanos"
    
    #=============== Part 3 - Session Mangement.(Find if exisiting.If not create new session)
    # check for existing sessions for this user
    existing_sessions = database_session_service.list_sessions(app_name=APP_NAME,user_id=USER_ID)
    if existing_sessions and len(existing_sessions.sessions)>0:
        # use the most recent session
        SESSION_ID = existing_sessions.sessions[0].id
        print(f"Continuing with SESSION_ID: {SESSION_ID}")
    else:
        # create a new session with initial state
        new_session = database_session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            state=_initial_state_
        )
        SESSION_ID = new_session.id
        print(f"Created new session: {SESSION_ID}")

    #=============== Part 4 - Agent runner setup
    # Create a runner with the memory agent
    runner = Runner(
        app_name=APP_NAME,
        session_service=database_session_service,
        agent=memory_agent
    )


    #=============== Part 5 - interactive conversation loop
    print("\nWelocme to Memory agent Chat!")
    print("\nYour reminders will be remebered across conversations.")
    print("\nType 'exit' or 'quit' to end the conversation")


    while True:
        # Get user input
        user_input = input("You :")

        # Check if the user wants to exit
        if user_input.lower() in ["exit","quit"]:
            print("Ending conversation.Your data has been saved to the database.")
            break

        #process the user query through the agent




if __name__ == "__main__":
    asyncio.run(main_async)