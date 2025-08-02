import os
from agents import Agent , function_tool
from dotenv import load_dotenv

from pydantic import BaseModel
from .agents import UserContext, restart_service_tool, restart_service_is_enabled

class UserContext(BaseModel):
    name: str
    is_premium_user: bool
    issue_type: str  
class TechnicalSupportAgentClass:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

    def handle(self, context: UserContext):
        if restart_service_is_enabled(context):
            return restart_service_tool(context)
        return "Restart tool only available for technical issues."

