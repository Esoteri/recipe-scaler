import math


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
