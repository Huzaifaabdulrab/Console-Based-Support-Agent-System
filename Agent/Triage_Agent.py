from .agents import UserContext
from .Billing_Agent import BillingAgentClass
from .TechnicalSupportAgent import TechnicalSupportAgentClass
from .General_Agent import GeneralSupportAgentClass

class TriageAgent:
    def __init__(self, billing_agent, technical_agent, general_agent):
        self.billing_agent = billing_agent
        self.technical_agent = technical_agent
        self.general_agent = general_agent

    def route(self, context, stream=False):
        issue = context.issue_type.lower()
        if "refund" in issue or "billing" in issue:
            if stream:
                return self.billing_agent.handle(context), "Billing Agent"
            return self.billing_agent.handle(context)
        elif "technical" in issue or "restart" in issue:
            if stream:
                return self.technical_agent.handle(context), "Technical Support Agent"
            return self.technical_agent.handle(context)
        else:
            if stream:
                return self.general_agent.handle(context), "General Agent"
            return self.general_agent.handle(context)