from django import forms
from .models import Collection, Flashcard

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

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['english_word', 'russian_translation']
        widgets = {
            'english_word': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Английское слово'
            }),
            'russian_translation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Русский перевод'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'initial' in kwargs and 'collection' in kwargs['initial']:
            self.fields.pop('collection', None)