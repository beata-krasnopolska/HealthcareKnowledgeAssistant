import json
from pathlib import Path

class GlossaryTool:
    def __init__(self, glossary_path: str = "data/tools/healthcare_glossary.json") -> None:
        self.glossary_path = Path(glossary_path)
        
    def _load_glossary(self) -> dict[str, str]:
        if not self.glossary_path.exists():
            return {}
        
        with self.glossary_path.open("r", encoding="utf-8") as file:
            return json.load(file)
        
    def lookup_term(self, term:str) -> str:
        glossary = self._load_glossary()
        normalized_term = term.strip().lower()
        
        if normalized_term in glossary:
            return glossary[normalized_term]
        
        return f"No glossary entry found for '{term}'."