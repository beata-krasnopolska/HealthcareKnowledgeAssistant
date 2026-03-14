from app.tools.contact_tool import ContactLookupTool
from app.tools.glossary_tool import GlossaryTool


class ToolRegistry:
    def __init__(self) -> None:
        self.glossary_tool = GlossaryTool()
        self.contact_lookup_tool = ContactLookupTool()