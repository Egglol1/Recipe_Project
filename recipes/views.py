from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists and details
import pandas as pd
from .models import Recipe, Ingredient                #to access Book model
from .forms import IngredientSearchForm
from .utils import get_chart, get_ingredientname_from_id
#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
  return render(request, 'recipes/home.html')

class RecipeListView(LoginRequiredMixin, ListView):           #class-based view
   model = Recipe                         #specify model
   template_name = 'recipes/main.html'    #specify template 

   def get_context_data(self, *args, **kwargs):
      context = super(RecipeListView, self).get_context_data(*args, **kwargs)
      context["form"] = IngredientSearchForm(None)
      return context

   def post(self, request):
      form = IngredientSearchForm(request.POST or None)
      recipes_df = None
      chart = None

      recipe_title = request.POST.get('recipe_title')
      ingredient_title = request.POST.get('ingredient_title')
      chart_type = request.POST.get('chart_type')

      qs = Recipe.objects.filter(
         name__icontains=recipe_title, ingredients__name__icontains=ingredient_title
         ).distinct()
      ingredient_qs = Ingredient.objects.filter(
         recipes__name__icontains=recipe_title,
         name__icontains=ingredient_title,
         ).distinct()
      if qs or ingredient_qs:
         recipes_df = pd.DataFrame(qs.values())
         ingredients_df = pd.DataFrame(ingredient_qs.values())
         ingredients_df['ingredient_name'] = ingredients_df['id'].apply(
            get_ingredientname_from_id
         )
         chart = get_chart(chart_type, recipes_df, ingredients_df=ingredients_df)
         recipes_df = recipes_df[['name', 'cooking_time', 'difficulty', 'id']]
         recipes_df = recipes_df.to_dict(orient='records')

      context = {
         'form': form,
         'recipes_df': recipes_df,
         'chart': chart
      }

      #load html page with all prepared data
      return render(request, 'recipes/main.html', context)

class RecipeDetailView(LoginRequiredMixin, DetailView):                       #class-based view
   model = Recipe                                        #specify model
   template_name = 'recipes/detail.html'                 #specify template