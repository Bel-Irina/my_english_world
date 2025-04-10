from django import forms
from .models import Collection, Flashcard
from django.core.exceptions import ValidationError

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название коллекции'
            })
        }
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name.strip()) < 3:
            raise ValidationError("Название должно содержать минимум 3 символа")
        return name

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['english_word', 'russian_translation', 'collection']
        widgets = {
            'english_word': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Английское слово'
            }),
            'russian_translation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Русский перевод'
            }),
            'collection': forms.Select(attrs={
                'class': 'form-control'
            })
        }
    
    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('english_word'):
            raise ValidationError("Английское слово обязательно")
        if not cleaned_data.get('russian_translation'):
            raise ValidationError("Русский перевод обязателен")
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'initial' in kwargs and 'collection' in kwargs['initial']:
            self.fields.pop('collection', None)

def clean_english_word(self):
    word = self.cleaned_data['english_word']
    if not word.strip():
        raise ValidationError("Поле обязательно для заполнения")
    return word