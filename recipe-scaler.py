# Recipe scaler v0.1
# Creates a dictionary for a recipe with ingredients and their quantities
# Then scales the recipe by a given factor
import math

recipe = {
    "fresh basil leaves": 3,
    "chopped walnuts": 1.5,
    "grated parmesan cheese": 0.25,
    "garlic cloves": 4,
    "olive oil": 1,
}

print("Original recipe", recipe)


# Perform recipe scaling
def scale_recipe(recipe, scaling_factor):
    if not math.isfinite(scaling_factor) or scaling_factor <= 0:
        raise ValueError("Scaling factor must be a finite number greater than zero.")

    return {
        ingredient: quantity * scaling_factor for ingredient, quantity in recipe.items()
    }


# Collect scaling factor from user input with validation
def get_scaling_factor():
    while True:
        user_input = input("Enter a scaling factor: ")

        try:
            scaling_factor = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        if not math.isfinite(scaling_factor) or scaling_factor <= 0:
            print("Invalid input. Please enter a finite number.")
            continue
        return scaling_factor


scaling_factor = get_scaling_factor()

scaled_recipe = scale_recipe(recipe, scaling_factor)
print("Scaled recipe", scaled_recipe)
