from datetime import date

from django.test import TestCase

from apps.chat.services import ChatbotService
from apps.knowledge.models import KnowledgeCategory, KnowledgeItem


class ChatbotServiceTests(TestCase):
    def setUp(self):
        self.category = KnowledgeCategory.objects.create(
            name="Propriedade Intelectual",
            slug="propriedade-intelectual",
            description="Orientação sobre proteção intelectual",
        )
        KnowledgeItem.objects.create(
            category=self.category,
            question="propriedade intelectual",
            variations="registro de patente\npatente e registro",
            answer="A AGINOV pode orientar sobre propriedade intelectual, incluindo conceitos básicos de registros, patentes e proteção de criação.",
            source_title="AGINOV",
            source_url="https://aginov.unemat.br",
            reviewed_at=date(2026, 8, 4),
            is_active=True,
        )

    def test_returns_answer_for_known_question(self):
        response = ChatbotService().answer("como posso obter orientação sobre propriedade intelectual?")

        self.assertEqual(response["status"], "answered")
        self.assertIn("propriedade intelectual", response["message"].lower())
        self.assertEqual(response["source"]["title"], "AGINOV")

    def test_returns_fallback_for_unknown_question(self):
        response = ChatbotService().answer("quero saber sobre algo totalmente diferente")

        self.assertEqual(response["status"], "fallback")
        self.assertIn("canal oficial", response["message"].lower())
