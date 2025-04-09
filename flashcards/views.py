from django.shortcuts import render, redirect, get_object_or_404
from .models import Collection, Flashcard
from .forms import CollectionForm, FlashcardForm

def home(request):
    flashcards = Flashcard.objects.all()
    collections = Collection.objects.all()
    return render(request, 'flashcards/home.html', {
        'flashcards': flashcards,
        'collections': collections
    })

def collection_detail(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)
    flashcards = Flashcard.objects.filter(collection=collection)
    collections = Collection.objects.all()
    return render(request, 'flashcards/collection_detail.html', {
        'collection': collection,
        'flashcards': flashcards,
        'collections': collections
    })

def add_collection(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CollectionForm()
    
    collections = Collection.objects.all()
    return render(request, 'flashcards/add_collection.html', {
        'form': form,
        'collections': collections
    })

def add_flashcard(request):
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FlashcardForm()
    
    collections = Collection.objects.all()
    return render(request, 'flashcards/add_flashcard.html', {
        'form': form,
        'collections': collections,
        'current_collection': None
    })

def delete_collection(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)
    if request.method == 'POST':
        collection.delete()
        return redirect('home')
    return redirect('home')

def delete_flashcard(request, flashcard_id):
    flashcard = get_object_or_404(Flashcard, id=flashcard_id)
    if request.method == 'POST':
        flashcard.delete()
        return redirect('home')
    return redirect('home')

def add_flashcard_to_collection(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)
    
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.collection = collection
            flashcard.save()
            return redirect('collection_detail', collection_id=collection.id)
    else:
        form = FlashcardForm(initial={'collection': collection})
    
    collections = Collection.objects.all()
    return render(request, 'flashcards/add_flashcard.html', {
        'form': form,
        'collections': collections,
        'current_collection': collection
    })