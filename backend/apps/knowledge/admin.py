from django.contrib import admin

from .models import KnowledgeCategory, KnowledgeItem


@admin.register(KnowledgeCategory)
class KnowledgeCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")


@admin.register(KnowledgeItem)
class KnowledgeItemAdmin(admin.ModelAdmin):
    list_display = ("question", "category", "is_active", "reviewed_at")
    list_filter = ("is_active", "category")
    search_fields = ("question", "answer", "source_title")
