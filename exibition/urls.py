from django.urls import path
from . import views

app_name = 'exibition'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('thank_you/', views.thank_you, name='thank-you'),
    path('owner/', views.OwnerList.as_view(), name='owner-list'),
    path('owner_create/', views.OwnerCreateView.as_view(), name='owner-create'),
    path('owner_update/<int:pk>',
         views.OwnerUpdateView.as_view(), name='owner-update'),
    path('owner_delete/<int:pk>',
         views.OwnerDeleteView.as_view(), name='owner-delete'),
    path('owner/<int:pk>/', views.OwnerDetailView.as_view(), name='owner-detail'),
    path('breed/', views.BreedList.as_view(), name='breed-list'),
    path('breed_create/', views.BreedCreateView.as_view(), name='breed-create'),
    path('breed_update/<int:pk>',
         views.BreedUpdateView.as_view(), name='breed-update'),
    path('breed_delete/<int:pk>',
         views.BreedDeleteView.as_view(), name='breed-delete'),
    path('breed/<int:pk>/', views.BreedDetailView.as_view(), name='breed-detail'),
    path('dogs/', views.DogList.as_view(), name='dog-list'),
    path('dog_create/', views.DogCreateView.as_view(), name='dog-create'),
    path('dog_update/<int:pk>',
         views.DogUpdateView.as_view(), name='dog-update'),
    path('dog_delete/<int:pk>',
         views.DogDeleteView.as_view(), name='dog-delete'),
    path('dogs/<int:pk>/', views.DogDetailView.as_view(), name='dog-detail'),
    path('judges/', views.JudgeList.as_view(), name='judge-list'),
    path('shows/', views.ShowList.as_view(), name='show-list'),
    path('sponsors/', views.SponsorList.as_view(), name='sponsor-list'),
]
