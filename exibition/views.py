from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Breed, Dog, Owner, Judge, Show, Sponsor


class HomeView(TemplateView):
    template_name = 'exibition/home.html'


class OwnerList(ListView):
    model = Owner
    template_name = 'exibition/owner_list'
    context_object_name = 'owners'


class BreedList(ListView):
    model = Breed
    template_name = 'exibition/breed_list'
    context_object_name = 'breeds'


class DogList(ListView):
    model = Dog
    template_name = 'exibition/dog_list'
    context_object_name = 'dogs'


class JudgeList(ListView):
    model = Judge
    template_name = 'exibition/judge_list'
    context_object_name = 'judges'


class ShowList(ListView):
    model = Show
    template_name = 'exibition/show_list'
    context_object_name = 'shows'


class SponsorList(ListView):
    model = Sponsor
    template_name = 'exibition/sponsor_list'
    context_object_name = 'sponsors'
