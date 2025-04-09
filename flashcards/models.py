from django.db import models
from django.core.validators import MinLengthValidator

class Collection(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3, "Название должно быть длиннее 3 символов")]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Flashcard(models.Model):
    english_word = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(1, "Слово не может быть пустым")]
    )
    russian_translation = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(1, "Перевод не может быть пустым")]
    )
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.english_word} - {self.russian_translation}"