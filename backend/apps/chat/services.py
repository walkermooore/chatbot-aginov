import re
from typing import Dict, Any


class ChatbotService:
    def __init__(self) -> None:
        self.knowledge_items = [
            {
                "keywords": ["propriedade", "intelectual", "registro", "patente"],
                "answer": "A AGINOV pode orientar sobre propriedade intelectual, incluindo conceitos básicos de registros, patentes e proteção de criação.",
                "category": "propriedade-intelectual",
                "source": {
                    "title": "AGINOV",
                    "url": "https://aginov.unemat.br",
                    "reviewed_at": "2026-08-04",
                },
            },
            {
                "keywords": ["inovacao", "ideia", "empreendedorismo", "prototipo"],
                "answer": "A AGINOV pode ajudar a entender caminhos de inovação, apoio institucional e encaminhamento para iniciativas empreendedoras.",
                "category": "inovacao",
                "source": {
                    "title": "AGINOV",
                    "url": "https://aginov.unemat.br",
                    "reviewed_at": "2026-08-04",
                },
            },
        ]

    def _normalize(self, question: str) -> str:
        text = question.lower()
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def answer(self, question: str) -> Dict[str, Any]:
        normalized = self._normalize(question)

        for item in self.knowledge_items:
            if any(keyword in normalized for keyword in item["keywords"]):
                return {
                    "status": "answered",
                    "message": item["answer"],
                    "category": item["category"],
                    "source": item["source"],
                }

        return {
            "status": "fallback",
            "message": "Não encontrei uma resposta segura na base disponível. Consulte o canal oficial da AGINOV para orientação adicional.",
            "official_channel": {
                "label": "Canal oficial da AGINOV",
                "url": "https://aginov.unemat.br",
            },
        }
