# Recipe scaler v0.1
# Creates a dictionary for a recipe with ingredients and their quantities
# Then scales the recipe by a given factor
recipe = {
    "fresh basil leaves": 3,
    "chopped walnuts": 1.5,
    "grated parmesan cheese": 0.25,
    "garlic cloves": 4,
    "olive oil": 1,
}

print("Original recipe", recipe)


def scale_recipe(recipe, scaling_factor):
    return {
        ingredient: quantity * scaling_factor for ingredient, quantity in recipe.items()
    }


scaled_recipe = scale_recipe(recipe, 2)
print("Scaled recipe", scaled_recipe)
