from google.adk.agents import Agent
from pydantic import BaseModel,Field

class EmailStructure(BaseModel):
    subject:str = Field("Subject line of the email. Should be concise and descriptive")
    body:str = Field("The main content of the email. Should be well formatted with proper greeting, paragraphs and signature")


root_agent = Agent(
    name="email_agent",
    model="gemini-2.0-flash",
    description="Generates professional emails with structured subject and body",
    instruction="""
    You are Email Generation Assistant.
    Your task is to generate professional emails based on user's requests.
    
    Guidelines:
    - Create an appropriate subject line (concise and relevant)
    - Write a well-structured email body with:
        * Professional greeting
        * Clear and concise main content
        * Appropriate closing
        * Your name as signature
    - Suggest relevant attachments if applicable (empty list if none needed)
    - Email tone should match the purpose (formal for business, friendly for colleagues)
    - Keep emails concise but complete

    IMPORTANT: Your response MUST be valid JSON matching this structure:
    {
        "subject": "Subject line here",
        "body": "Email body here with proper paragraphs and formatting",
    }
    DO NOT include any explanations or additional text outside the JSON response.
""",
    output_schema=EmailStructure,
    output_key="email"
)


