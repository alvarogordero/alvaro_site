from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import (TemplateView)
from django.urls import reverse_lazy


# Create your views here.
class AboutView(TemplateView):
    template_name = 'blog/about.html'


class HomeView(TemplateView):
    template_name = "blog/home.html"


class ItfView(TemplateView):
    template_name = 'blog/itf.html'


class MetconView(TemplateView):
    template_name = 'blog/new_metcon_area.html'

class MybikeView(TemplateView):
    template_name = 'blog/mybike.html'

class DislexiaView(TemplateView):
    template_name = 'blog/dislexia.html'
