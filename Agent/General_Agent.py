from .agents import UserContext, get_faqs_tool

class GeneralSupportAgentClass:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

    def handle(self, context: UserContext):
        return get_faqs_tool(context)
