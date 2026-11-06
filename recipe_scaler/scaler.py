import math


# Perform recipe scaling
def scale_recipe(recipe, scaling_factor):
    if not math.isfinite(scaling_factor) or scaling_factor <= 0:
        raise ValueError("Scaling factor must be a finite number greater than zero.")

    return {
        ingredient: quantity * scaling_factor
        for ingredient, quantity in recipe.items()
    }
