from google.genai import types
from google.adk.runners import Runner

# ANSI color codes for terminal output
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    # Foreground colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Background colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"


async def display_state():
    pass

async def process_agent_event():
    pass

async def call_agent_async(runner:Runner,user_id,session_id,query):
    """Call the agent asynchronously with user's query"""


    message = types.Content(role="user",parts=[types.Part(text=query)])

    print(f"\n{Colors.BG_GREEN}{Colors.BLACK}{Colors.BOLD}--- Running Query:{query} ----{Colors.RESET}")

    final_response_text = None

    # display state before processing
    display_state()

    try:
        async for events in runner.run(
            user_id=user_id,
            session_id=session_id,
            new_message=message
        ):
            # Process each req and get the final response if available
            response = await process_agent_event(event)
            if response:
                final_response_text = response
    
    except Exception as e:
        print(f"Error during agent call: {e}")


    # displat state after processing the message
    display_state()

    return final_response_text