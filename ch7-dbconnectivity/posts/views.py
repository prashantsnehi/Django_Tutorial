from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView
from .models import Post, Employees

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    
class EmployeesPageView(ListView):
    model = Employees
    template_name = 'employees.html'
    
class AbouutPageView(TemplateView):
    template_name = 'about.html'
    
class EmployeesPageView(TemplateView):
    template_name = 'employees.html'
