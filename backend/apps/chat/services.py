import re
from typing import Dict, Any

from apps.knowledge.models import KnowledgeItem


class ChatbotService:
    def _normalize(self, question: str) -> str:
        text = question.lower()
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def answer(self, question: str) -> Dict[str, Any]:
        normalized = self._normalize(question)

        items = (
            KnowledgeItem.objects.filter(is_active=True)
            .select_related("category")
            .order_by("id")
        )

        if not items.exists():
            return {
                "status": "fallback",
                "message": "Não encontrei uma resposta segura na base disponível. Consulte o canal oficial da AGINOV para orientação adicional.",
                "official_channel": {
                    "label": "Canal oficial da AGINOV",
                    "url": "https://aginov.unemat.br",
                },
            }

        for item in items:
            for candidate in [item.question, *item.variations_list]:
                if self._normalize(candidate) in normalized:
                    return {
                        "status": "answered",
                        "message": item.answer,
                        "category": item.category.slug,
                        "source": {
                            "title": item.source_title,
                            "url": item.source_url or "https://aginov.unemat.br",
                            "reviewed_at": item.reviewed_at.isoformat(),
                        },
                    }

        return {
            "status": "fallback",
            "message": "Não encontrei uma resposta segura na base disponível. Consulte o canal oficial da AGINOV para orientação adicional.",
            "official_channel": {
                "label": "Canal oficial da AGINOV",
                "url": "https://aginov.unemat.br",
            },
        }
