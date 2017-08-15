from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from catalog import forms
from catalog import models

# Create your views here.
class BandCreateView(CreateView):
    form_class = forms.BandCreateForm
    template_name = 'band/create.html'
    model = models.Band

    def get_success_url(self):
        return reverse('BandListView')

class BandListView(ListView):
    model = models.Band
    template_name = 'band/list.html'

class BandUpdateView(UpdateView):
    model = models.Band
    template_name = 'band/create.html'
    form_class = forms.BandCreateForm

    def get_success_url(self):
        return reverse('BandListView')

class BandDeleteView(DeleteView):
    model = models.Band
    template_name = 'band/delete.html'

    def get_success_url(self):
        return reverse('BandListView')