from django.test import TestCase
from .models import Recipe, Ingredient
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import IngredientSearchForm

# Create your tests here.

class RecipeModelTest(TestCase):
  def setUpTestData():
    tea_leaves = Ingredient.objects.create(name="tea-leaves")
    water = Ingredient.objects.create(name="water")
    sugar = Ingredient.objects.create(name="sugar")
    pic = SimpleUploadedFile(
            "..\static\recipes\Images\Tea.jpg", content=b"", content_type="image/jpeg"
        )
    recipe = Recipe.objects.create(name='Tea',  cooking_time = 5, difficulty='easy', pic=pic)
    recipe.ingredients.set([tea_leaves, water, sugar])

  def test_recipe_name(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('name').verbose_name
    self.assertEqual(field_label, 'name')

  def test_recipe_cooking_time(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('cooking_time').verbose_name
    self.assertEqual(field_label, 'cooking time')

  def test_recipe_ingredients(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('ingredients').verbose_name
    self.assertEqual(field_label, 'ingredients')

  def test_recipe_difficulty(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('difficulty').verbose_name
    self.assertEqual(field_label, 'difficulty')

  def test_get_absolute_url(self):
    recipe = Recipe.objects.get(id=1)
    self.assertEqual(recipe.get_absolute_url(), '/list/1')

class RecipeFormTest(TestCase):       
   def test_recipe_form(self):
      form_data = {'recipe_title': 'tea', 'ingredient_title': 'water', 'chart_type': '#1'}
      form = IngredientSearchForm(data=form_data)
      self.assertTrue(form.is_valid())
      
   def test_recipe_form_invalid_chart(self):
      form_data = {'recipe_title': 'tea', 'ingredient_title': 'water', 'chart_type': '#4'}
      form = IngredientSearchForm(data=form_data)
      self.assertFalse(form.is_valid())
      
   def test_recipe_form_invalid_recipe_title(self):
      form_data = {'recipe_title': '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 'ingredient_title': 'water', 'chart_type': '#1'}
      form = IngredientSearchForm(data=form_data)
      self.assertFalse(form.is_valid())
      
   def test_recipe_form_invalid_ingredient_title(self):
      form_data = {'recipe_title': 'tea', 'ingredient_title': '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 'chart_type': '#1'}
      form = IngredientSearchForm(data=form_data)
      self.assertFalse(form.is_valid())
        
   def test_recipe_form_missing_ingredient_title(self):
      form_data = {'recipe_title': 'tea', 'ingredient_title': '', 'chart_type': '#1'}
      form = IngredientSearchForm(data=form_data)
      self.assertTrue(form.is_valid())
      
   def test_recipe_form_missing_recipe_title(self):
      form_data = {'recipe_title': '', 'ingredient_title': 'water', 'chart_type': '#1'}
      form = IngredientSearchForm(data=form_data)
      self.assertTrue(form.is_valid())