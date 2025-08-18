from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

def get_current_date_time()->dict:
    "Get the current time and date in the format YYY-MM-DD";

    return {
        "current_time:" : datetime.today().strftime('%Y-%m-%d')
    }

root_agent = Agent(
    name ="tool_agent",
    model="gemini-2.0-flash",
    description=(
        "Tool agent"
        ),
    instruction="""
    You are a helpful assistant that can use the following tools:
    - get_current_date_time
    """,
    # instruction="""
    # You are a helpful assistant that can use the following tools:
    # - google_search
    # """,
    # tools=[google_search]
    tools=[get_current_date_time]
    # tools=[google_search,get_current_date_time] - we can't have both third party/custom tools with built in tools(google_search). built in toolls only work with gemini models
)