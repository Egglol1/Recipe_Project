from django.test import TestCase
from .models import Recipe, Ingredient
from django.core.files.uploadedfile import SimpleUploadedFile

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