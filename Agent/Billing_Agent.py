import os
from agents import Agent , function_tool
from dotenv import load_dotenv
from pydantic import BaseModel
from .agents import UserContext, refund_tool, refund_is_enabled

class UserContext(BaseModel):
    name: str
    is_premium_user: bool
    issue_type: str  

class BillingAgentClass:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

    def handle(self, context: UserContext):
        if refund_is_enabled(context):
            return refund_tool(context)
        return "Refund tool not available for non-premium users."
