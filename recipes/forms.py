from django import forms

CHART__CHOICES = (
  ('#1', 'Bar Chart'),
  ('#2', 'Pie Chart'),
  ('#3', 'Line Chart')
)

class IngredientSearchForm(forms.Form): 
   recipe_title= forms.CharField(max_length=120, required=False)
   ingredient_title= forms.CharField(max_length=120, required=False)
   chart_type = forms.ChoiceField(choices=CHART__CHOICES)