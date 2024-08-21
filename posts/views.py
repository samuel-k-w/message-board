from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
# Create your views here.

class HomePageView(TemplateView):
  model = Post
  template_name = 'home.html'