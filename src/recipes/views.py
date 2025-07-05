from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists and details
from .models import Recipe                #to access Book model
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
  return render(request, 'recipes/home.html')

class RecipeListView(LoginRequiredMixin, ListView):           #class-based view
   model = Recipe                         #specify model
   template_name = 'recipes/main.html'    #specify template 

class RecipeDetailView(LoginRequiredMixin, DetailView):                       #class-based view
   model = Recipe                                        #specify model
   template_name = 'recipes/detail.html'                 #specify template