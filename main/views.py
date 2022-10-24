from django.views.generic import TemplateView
from django.shortcuts import render


class Index(TemplateView):
    template_name = 'main/index.html'


class Category(TemplateView):
    template_name = 'main/category.html'
