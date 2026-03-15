from app.tools.glossary_tool import GlossaryTool


def glossary_tool_returns_definition():
    tool = GlossaryTool()
    
    result = tool.lookup_term("referral")
    
    assert "primary care provider" in result.lower() or "specialist" in result.lower()
    
def glossary_tool_returns_fallback_for_unknown_term():
    tool = GlossaryTool()
    
    result = tool.lookup.term("unknown term")
    assert "no glossary entry found" in result.lower()