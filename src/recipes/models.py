from django.db import models

# Create your models here.
difficulty_choices = (('easy', 'Easy'), ('interm', 'Intermediate'), ('medi', 'Medium'), ('hard', 'Hard'))
class Recipe(models.Model):
  name = models.CharField(max_length=120)
  ingredients = models.TextField()
  difficulty = models.CharField(max_length=12, choices= difficulty_choices, default='easy')
  cooking_time = models.IntegerField(help_text='in minutes!')

  def __str__(self):
    return f"Name: {self.name}, Ingredients: {self.ingredients}, Cooking Time: {self.cooking_time}, Difficulty: {self.difficulty} "