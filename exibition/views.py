from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Breed, Dog, Owner, Judge, Show, Sponsor


class HomeView(TemplateView):
    template_name = 'exibition/home.html'


class OwnerList(ListView):
    model = Owner
    template_name = 'exibition/owner_list.html'
    context_object_name = 'owners'


def thank_you(request):
    return render(request, 'exibition/thank_you.html')


class OwnerDetailView(DetailView):
    model = Owner
    template_name = 'exibition/owner_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        owner = self.get_object()
        context["dogs"] = Dog.objects.filter(owner=owner)
        return context


class OwnerCreateView(LoginRequiredMixin, CreateView):
    model = Owner
    fields = ['first_name', 'last_name', 'email',
              'phone', 'address', 'user']
    success_url = reverse_lazy('exibition:thank-you')

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         raise Http404("You must be logged in to access this page.")
    #     return super().dispatch(request, *args, **kwargs)


class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    model = Owner
    fields = fields = ['first_name', 'last_name',
                       'email', 'phone', 'address', 'user']
    success_url = reverse_lazy('exibition:owner-list')


class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    model = Owner
    success_url = reverse_lazy('exibition:owner-list')


class BreedList(ListView):
    model = Breed
    template_name = 'exibition/breed_list.html'
    context_object_name = 'breeds'


class BreedDetailView(DetailView):
    model = Breed


class BreedCreateView(LoginRequiredMixin, CreateView):
    model = Breed
    fields = ['name', 'description']
    success_url = reverse_lazy('exibition:thank-you')


class BreedUpdateView(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = ['name', 'description']
    success_url = reverse_lazy('exibition:breed-list')


class BreedDeleteView(LoginRequiredMixin, DeleteView):
    model = Breed
    success_url = reverse_lazy('exibition:breed-list')


class DogList(ListView):
    model = Dog
    template_name = 'exibition/dog_list'
    context_object_name = 'dogs'


class DogDetailView(DetailView):
    model = Dog


class DogCreateView(LoginRequiredMixin, CreateView):
    model = Dog
    fields = ['name', 'breed', 'gender', 'age',
              'weight', 'color', 'owner', 'breed', 'image']
    success_url = reverse_lazy('exibition:thank-you')


class DogUpdateView(LoginRequiredMixin, UpdateView):
    model = Dog
    fields = ['name', 'breed', 'gender', 'age',
              'weight', 'color', 'owner', 'breed', 'image']
    success_url = reverse_lazy('exibition:dog-list')


class DogDeleteView(LoginRequiredMixin, DeleteView):
    model = Dog
    fields = ['name', 'breed', 'gender', 'age',
              'weight', 'color', 'owner', 'breed']
    success_url = reverse_lazy('exibition:dog-list')


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
