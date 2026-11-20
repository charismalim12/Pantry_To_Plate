import pandas as pd

recipes = pd.read_csv("data/recipes.csv")
ingredients = pd.read_csv("data/ingredients_master.csv")
recipe_ingredients = pd.read_csv("data/recipe_ingredients.csv")

print("PANTRY TO PLATE")
print("============================")

print("Welcome to Pantry to Plate!")
print("Find recipes using ingredients you already have.")

print("Loading recipe database...")

print("Recipes loaded:", len(recipes))
print("Ingredients loaded:", len(ingredients))
print("Recipe ingredient records:", len(recipe_ingredients))
