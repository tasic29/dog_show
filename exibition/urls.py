from django.urls import path
from . import views

app_name = 'exibition'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('owner/', views.OwnerList.as_view(), name='owner-list'),
    path('breed/', views.BreedList.as_view(), name='breed-list'),
    path('dogs/', views.DogList.as_view(), name='dog-list'),
    path('judges/', views.JudgeList.as_view(), name='judge-list'),
    path('shows/', views.ShowList.as_view(), name='show-list'),
    path('sponsors/', views.SponsorList.as_view(), name='sponsor-list'),
]
