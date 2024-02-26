from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Breed, Dog, Owner, Judge, Show, Sponsor


class HomeView(TemplateView):
    template_name = 'exibition/home.html'


class OwnerList(ListView):
    model = Owner
    template_name = 'exibition/owner_list'
    context_object_name = 'owners'


class OwnerDetailView(DetailView):
    model = Owner
    template_name = 'exibition/owner_detail.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        owner = self.get_object()
        context["dogs"] = Dog.objects.filter(owner=owner)
        return context


class BreedList(ListView):
    model = Breed
    template_name = 'exibition/breed_list'
    context_object_name = 'breed_list'


class BreedDetailView(DetailView):
    model = Breed


class DogList(ListView):
    model = Dog
    template_name = 'exibition/dog_list'
    context_object_name = 'dogs'


class DogDetailView(DetailView):
    model = Dog


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
