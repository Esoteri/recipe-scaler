# Recipe scaler v0.1
# Creates a dictionary for a recipe with ingredients and their quantities
# Then scales the recipe by a given factor
from recipe_scaler.cli import get_scaling_factor
from recipe_scaler.scaler import scale_recipe

recipe = {
    "fresh basil leaves": 3,
    "chopped walnuts": 1.5,
    "grated parmesan cheese": 0.25,
    "garlic cloves": 4,
    "olive oil": 1,
}


def main():
    print("Original recipe", recipe)

    scaling_factor = get_scaling_factor()

    scaled_recipe = scale_recipe(recipe, scaling_factor)
    print("Scaled recipe", scaled_recipe)


if __name__ == "__main__":
    main()
