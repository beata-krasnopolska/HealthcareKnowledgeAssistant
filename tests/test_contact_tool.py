from app.tools.contact_tool import ContactLookupTool


def test_contact_lookup_returns_department_details():
    tool = ContactLookupTool()
    result = tool.lookup_department("privacy office")
    assert result is not None
    assert "privacy office" in result.lower()
    
def test_contact_lookup_returns_fallback_for_unknown_department():
    tool = ContactLookupTool()
    
    result = tool.lookup_department("unknown department")
    assert result is not None
    assert "no contact information found for department" in result.lower()