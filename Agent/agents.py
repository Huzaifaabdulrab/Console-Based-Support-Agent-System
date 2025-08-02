from pydantic import BaseModel

class UserContext(BaseModel):
    name: str
    is_premium_user: bool
    issue_type: str

def refund_tool(context: UserContext):
    return "Refund process initiated."

def refund_is_enabled(context: UserContext):
    return context.is_premium_user

def restart_service_tool(context: UserContext):
    return "Service restart initiated."

def restart_service_is_enabled(context: UserContext):
    return context.issue_type == "technical"

def get_faqs_tool(context: UserContext):
    return "Here are the FAQs: [list of FAQs]"