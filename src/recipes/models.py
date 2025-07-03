from django.db import models
from django.shortcuts import reverse

# Create your models here.
difficulty_choices = (('easy', 'Easy'), ('interm', 'Intermediate'), ('medi', 'Medium'), ('hard', 'Hard'))

class Ingredient(models.Model):
  name = models.CharField(max_length=120, unique=True)

  def __str__(self):
    return self.name

class Recipe(models.Model):
  name = models.CharField(max_length=120)
  description = models.TextField(max_length=500, default='Please describe your recipe.')
  ingredients = models.ManyToManyField(Ingredient)
  difficulty = models.CharField(max_length=12, choices= difficulty_choices, default='easy')
  cooking_time = models.IntegerField(help_text='in minutes!')
  pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

  def __str__(self):
    return f"Name: {self.name}, Ingredients: {self.ingredients.name}, Cooking Time: {self.cooking_time}, Difficulty: {self.difficulty} "
  def get_absolute_url(self):
    return reverse ('recipes:detail', kwargs={'pk': self.pk})