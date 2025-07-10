from recipes.models import (
    Recipe,
    Ingredient,
)
from io import BytesIO 
import base64
import matplotlib.pyplot as plt

def get_recipename_from_id(val):
    # this ID is used to retrieve the name from the record
    recipename = Recipe.objects.get(id=val)
    # and the name is returned back
    return recipename

def get_ingredientname_from_id(val):
    # this ID is used to retrieve the ingredient name from the record
    ingredientname = Ingredient.objects.get(id=val).name
    # and the name is returned back
    return ingredientname

def get_graph():
   #create a BytesIO buffer for the image
   buffer = BytesIO()         

   #create a plot with a bytesIO object as a file-like object. Set format to png
   plt.savefig(buffer, format='png')

   #set cursor to the beginning of the stream
   buffer.seek(0)

   #retrieve the content of the file
   image_png=buffer.getvalue()

   #encode the bytes-like object
   graph=base64.b64encode(image_png)

   #decode to get the string as output
   graph=graph.decode('utf-8')

   #free up the memory of buffer
   buffer.close()

   #return the image/graph
   return graph

#chart_type: user input type of chart,
#data: pandas dataframe
def get_chart(chart_type, data, **kwargs):
   #switch plot backend to AGG (Anti-Grain Geometry) - to write to file
   #AGG is preferred solution to write PNG files
   plt.switch_backend('AGG')

   #specify figure size
   fig=plt.figure(figsize=(6,3))

   #select chart_type based on user input from the form
   if chart_type == "#1":
        ingredients_df = kwargs.get("ingredients_df")
        ingredients_groupby = ingredients_df.groupby("id").agg(
            {"ingredient_name": "first", "id": "count"}
        )
        # plot BAR CHART between date on x-axis and quantity on y-axis
        plt.bar(
            ingredients_groupby["ingredient_name"].values,
            ingredients_groupby["id"].values,
        )
        plt.xlabel("Ingredient Name")
        plt.ylabel("Number of Recipes")

   elif chart_type == '#2':
       difficulty_sizes = data.groupby("difficulty").agg(
            {"difficulty": "first", "id": "count"}
        )
       plt.pie(difficulty_sizes["id"].values, labels=difficulty_sizes["difficulty"].values)

   elif chart_type == '#3':
       #plot line chart based on date on x-axis and cooking_time on y-axis
       cooking_time_sizes = data.groupby("cooking_time").agg(
            {"cooking_time": "first", "id": "count"}
        )
       plt.plot(cooking_time_sizes["cooking_time"], cooking_time_sizes["id"])
       plt.xlabel("Cooking Time")
       plt.ylabel("Recipe Count")
   else:
       print ('unknown chart type')

   #specify layout details
   plt.tight_layout()

   #render the graph to file
   chart =get_graph() 
   return chart