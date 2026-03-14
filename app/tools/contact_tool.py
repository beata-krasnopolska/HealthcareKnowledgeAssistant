import json
from pathlib import Path

class ContactLookupTool:
    def __init__(self, contacts_path: str = "data/tools/department_contacts.json") -> None:
        self.contacts_path = Path(contacts_path)
        
    def _load_contacts(self) -> dict:
        if not self.contacts_path.exists():
            return {}
        
        with self.contacts_path.open("r", encoding="utf-8") as file:
            return json.load(file)
        
    def lookup_department(self, department_name: str) -> str:
        contacts = self._load_contacts()
        normalized_name = department_name.strip().lower()
        
        if normalized_name not in contacts:
            return f"No contact information found for department '{department_name}'."
        
        depafrtmant_info = contacts[normalized_name]
        
        return (
            f"Department: {department_name}\n"
            f"Phone: {depafrtmant_info.get('phone', 'N/A')}\n"
            f"Email: {depafrtmant_info.get('email', 'N/A')}\n"
        )