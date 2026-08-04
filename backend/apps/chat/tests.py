from django.test import SimpleTestCase

from apps.chat.services import ChatbotService


class ChatbotServiceTests(SimpleTestCase):
    def test_returns_answer_for_known_question(self):
        response = ChatbotService().answer("como posso obter orientação sobre propriedade intelectual?")

        self.assertEqual(response["status"], "answered")
        self.assertIn("propriedade intelectual", response["message"].lower())
        self.assertEqual(response["source"]["title"], "AGINOV")

    def test_returns_fallback_for_unknown_question(self):
        response = ChatbotService().answer("quero saber sobre algo totalmente diferente")

        self.assertEqual(response["status"], "fallback")
        self.assertIn("canal oficial", response["message"].lower())
