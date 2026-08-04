from django.db import models


class KnowledgeCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return self.name


class KnowledgeItem(models.Model):
    category = models.ForeignKey(KnowledgeCategory, on_delete=models.CASCADE, related_name="items")
    question = models.CharField(max_length=255)
    variations = models.TextField(blank=True, help_text="Variações separadas por linha")
    answer = models.TextField()
    source_title = models.CharField(max_length=200)
    source_url = models.URLField(blank=True)
    reviewed_at = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Item de conhecimento"
        verbose_name_plural = "Itens de conhecimento"

    def __str__(self) -> str:
        return self.question

    @property
    def variations_list(self):
        return [item.strip() for item in self.variations.splitlines() if item.strip()]
