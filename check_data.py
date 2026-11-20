import pandas as pd

# Load datasets
recipes = pd.read_csv("data/recipes.csv")
ingredients = pd.read_csv("data/ingredients_master.csv")
recipe_ingredients = pd.read_csv("data/recipe_ingredients.csv")

# Display dataset sizes
print("DATASET SIZES")
print("--------------------")
print("Total recipes:", len(recipes))
print("Total master ingredients:", len(ingredients))
print("Total recipe ingredient entries:", len(recipe_ingredients))

# Check required columns
print("\nREQUIRED COLUMNS")
print("--------------------")

print("Recipes:", recipes.columns.tolist())
print("Ingredients:", ingredients.columns.tolist())
print("Recipe Ingredients:", recipe_ingredients.columns.tolist())

# Check duplicate IDs
print("\nDUPLICATE CHECKS")
print("--------------------")
print("Duplicate recipe IDs:", recipes["recipe_id"].duplicated().sum())
print("Duplicate ingredient IDs:", ingredients["ingredient_id"].duplicated().sum())

# Check recipe IDs
recipe_ids = set(recipes["recipe_id"])
linked_recipe_ids = set(recipe_ingredients["recipe_id"])

print("\nRECIPE ID CHECK")
print("--------------------")
print("All recipe IDs exist:",
      linked_recipe_ids.issubset(recipe_ids))
print("Recipes without ingredients:",
      len(recipe_ids - linked_recipe_ids))

# Check ingredient IDs
ingredient_ids = set(ingredients["ingredient_id"])
linked_ingredient_ids = set(recipe_ingredients["ingredient_id"])

print("\nINGREDIENT ID CHECK")
print("--------------------")
print("All ingredient IDs exist:",
      linked_ingredient_ids.issubset(ingredient_ids))
print("Unused master ingredients:",
      len(ingredient_ids - linked_ingredient_ids))

# Check duplicate recipe-ingredient combinations
print("\nRELATIONSHIP CHECK")
print("--------------------")
print(
    "Duplicate recipe-ingredient combinations:",
    recipe_ingredients.duplicated(
        subset=["recipe_id", "ingredient_id"]
    ).sum()
)

# Check missing information
print("\nMISSING VALUES")
print("--------------------")
print("Recipes:")
print(recipes.isnull().sum())

print("\nIngredients:")
print(ingredients.isnull().sum())

print("\nRecipe Ingredients:")
print(recipe_ingredients.isnull().sum())

# Display sample recipes
print("\nSAMPLE RECIPES")
print("--------------------")
print(recipes.head(5))

# Check recipe quality
print("\nRECIPE QUALITY CHECK")
print("--------------------")

print("Unique recipe names:", recipes["recipe_name"].nunique())
print("Unique instructions:", recipes["instructions"].nunique())

print("\nRecipes by cuisine:")
print(recipes["cuisine"].value_counts())

print("\nMost common ingredients:")
ingredient_usage = recipe_ingredients["ingredient_id"].value_counts()
print(ingredient_usage.head(15))

print("\nSample recipe names:")
print(recipes["recipe_name"].head(20).to_string(index=False))

print("\nSample instructions:")
print(recipes["instructions"].head(3).to_string(index=False))

# Investigate most common ingredients
print("\nMOST COMMON INGREDIENT DETAILS")
print("--------------------")

common_ingredients = (
    recipe_ingredients["ingredient_id"]
    .value_counts()
    .head(10)
    .index
)

print(
    ingredients[
        ingredients["ingredient_id"].isin(common_ingredients)
    ].to_string(index=False)
)