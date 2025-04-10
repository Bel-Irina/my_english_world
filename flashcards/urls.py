from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('collections/add/', views.add_collection, name='add_collection'),
    path('collections/<int:collection_id>/', views.collection_detail, name='collection_detail'),
    path('collections/<int:collection_id>/add-word/', views.add_flashcard_to_collection, name='add_flashcard_to_collection'),
    path('collections/<int:collection_id>/delete/', views.delete_collection, name='delete_collection'),
    path('flashcards/add/', views.add_flashcard, name='add_flashcard'),
    path('flashcards/<int:flashcard_id>/delete/', views.delete_flashcard, name='delete_flashcard'),
    path('flashcards/add/', views.add_flashcard_to_collection, name='add_flashcard'),
    path('collections/<int:collection_id>/add-flashcard/', views.add_flashcard_to_collection, name='add_flashcard_to_collection'),
]