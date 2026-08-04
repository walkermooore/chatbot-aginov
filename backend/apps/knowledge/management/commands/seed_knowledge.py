from datetime import date

from django.core.management.base import BaseCommand

from apps.knowledge.models import KnowledgeCategory, KnowledgeItem


class Command(BaseCommand):
    help = "Popula a base de conhecimento inicial do chatbot"

    def handle(self, *args, **options):
        category_pi, _ = KnowledgeCategory.objects.get_or_create(
            slug="propriedade-intelectual",
            defaults={
                "name": "Propriedade Intelectual",
                "description": "Orientação sobre proteção intelectual e registros",
            },
        )
        KnowledgeItem.objects.get_or_create(
            question="propriedade intelectual",
            defaults={
                "category": category_pi,
                "variations": "registro de patente\npatente e registro",
                "answer": "A AGINOV pode orientar sobre propriedade intelectual, incluindo conceitos básicos de registros, patentes e proteção de criação.",
                "source_title": "AGINOV",
                "source_url": "https://aginov.unemat.br",
                "reviewed_at": date(2026, 8, 4),
                "is_active": True,
            },
        )

        category_innovation, _ = KnowledgeCategory.objects.get_or_create(
            slug="inovacao",
            defaults={
                "name": "Inovação",
                "description": "Apoio a ideias, protótipos e empreendedorismo",
            },
        )
        KnowledgeItem.objects.get_or_create(
            question="inovação",
            defaults={
                "category": category_innovation,
                "variations": "ideia\nprototipo\nempreendedorismo",
                "answer": "A AGINOV pode ajudar a entender caminhos de inovação, apoio institucional e encaminhamento para iniciativas empreendedoras.",
                "source_title": "AGINOV",
                "source_url": "https://aginov.unemat.br",
                "reviewed_at": date(2026, 8, 4),
                "is_active": True,
            },
        )

        self.stdout.write(self.style.SUCCESS("Base de conhecimento inicial carregada com sucesso."))
