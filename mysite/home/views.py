from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import homemenu

class IndexView(generic.ListView):
    model = homemenu
    template_name = 'home/index.html'


		