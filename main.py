import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig
from openai import AsyncOpenAI
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv
import asyncio
# Import agents
from Agent.agents import UserContext
from Agent.Billing_Agent import BillingAgentClass
from Agent.TechnicalSupportAgent import TechnicalSupportAgentClass
from Agent.General_Agent import GeneralSupportAgentClass
from Agent.Triage_Agent import TriageAgent

# Load API Key
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

# Model and config setup
provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=provider
)

run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

# Get user context
def get_user_context():
    name = input("Enter your name: ")
    is_premium = input("Are you a premium user? (yes/no): ").strip().lower() == "yes"
    issue_type = input("Describe your issue (e.g., refund, technical, billing, faq): ").strip()
    return UserContext(name=name, is_premium_user=is_premium, issue_type=issue_type)

def stream_output(text):
    for char in text:
        print(char, end="", flush=True)
    print()

def main():
    billing_agent = BillingAgentClass(
        name="BillingAgent",
        instructions="Handles billing issues and refunds."
    )
    technical_agent = TechnicalSupportAgentClass(
        name="TechnicalSupportAgent",
        instructions="Handles technical issues and service restarts."
    )
    general_agent = GeneralSupportAgentClass(
        name="GeneralAgent",
        instructions="Handles general questions and FAQs."
    )
    triage_agent = TriageAgent(billing_agent, technical_agent, general_agent)

    context = get_user_context()
    print("\nAgent is thinking...\n")
    result, handoff = triage_agent.route(context, stream=True)
    print(f"[System] Handoff to: {handoff}")
    print("[System] Executing tool...\n")
    stream_output(result)
    print("\n Final Response:\n", result)

if __name__ == "__main__":
    main()
