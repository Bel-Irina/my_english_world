from django.contrib import admin
from .models import Collection, Flashcard

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('english_word', 'russian_translation', 'collection')
    search_fields = ('english_word', 'russian_translation')
    list_filter = ('collection', 'created_at')