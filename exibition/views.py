from django.shortcuts import render
from django.urls import reverse_lazy
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


class OwnerCreateView(CreateView):
    model = Owner
    fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'user']
    success_url = reverse_lazy('exibition:thank-you')


class OwnerUpdateView(UpdateView):
    model = Owner
    fields = fields = ['first_name', 'last_name',
                       'email', 'phone', 'address', 'user']
    success_url = reverse_lazy('exibition:owner-list')


class OwnerDeleteView(DeleteView):
    model = Owner
    success_url = reverse_lazy('exibition:owner-list')


class BreedList(ListView):
    model = Breed
    template_name = 'exibition/breed_list.html'
    context_object_name = 'breeds'


class BreedDetailView(DetailView):
    model = Breed


class BreedCreateView(CreateView):
    model = Breed
    fields = ['name', 'description']
    success_url = reverse_lazy('exibition:thank-you')


class BreedUpdateView(UpdateView):
    model = Breed
    fields = ['name', 'description']
    success_url = reverse_lazy('exibition:breed-list')


class BreedDeleteView(DeleteView):
    model = Breed
    success_url = reverse_lazy('exibition:breed-list')


class DogList(ListView):
    model = Dog
    template_name = 'exibition/dog_list'
    context_object_name = 'dogs'


class DogDetailView(DetailView):
    model = Dog


class DogCreateView(CreateView):
    model = Dog
    fields = ['name', 'breed', 'gender', 'age',
              'weight', 'color', 'owner', 'breed']
    success_url = reverse_lazy('exibition:thank-you')


class DogUpdateView(UpdateView):
    model = Dog
    fields = ['name', 'breed', 'gender', 'age',
              'weight', 'color', 'owner', 'breed']
    success_url = reverse_lazy('exibition:dog-list')


class DogDeleteView(DeleteView):
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
