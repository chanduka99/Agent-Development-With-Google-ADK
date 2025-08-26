from google.adk.agents import Agent


faq_agent = Agent(
    name="faq_agent",
    model="gemini-2.0-flash",
    description="Answer questions asked by the user",
    instruction="""
    You are an agent that will give anwers to the user.
    
    Use the below information to answer the quesions:
    Name:{user_name},
    Preferences:{user_prefernces}

    IMPORTANT:
    - Do not show any json responses.
    """
)