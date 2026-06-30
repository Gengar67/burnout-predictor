Sleep_penalty = -5
coffee_penalty = -2
Work_penalty = 8
base_stress = 40

print("--- WELCOME TO THE TECH-BURNOUT CALCULATOR ---")

hours_slept = int(input("How many hours did you sleep? "))
hours_worked = int(input("How many hours did you work? "))

coffee_input = input("Did you drink coffee today? (Yes or No): ").lower()

if coffee_input == "yes" or coffee_input == "y":
   had_coffee = 1
else:
    had_coffee = 0

stress_level = base_stress + (Sleep_penalty * hours_slept) + (Work_penalty * hours_worked) + (had_coffee * coffee_penalty)

print("\n--- RESULTS ---")
if stress_level > 70:
    print(f"Your stress level is: {stress_level} - WARNING: High Burnout Risk!")
else:
    print(f"Your stress level is: {stress_level} - You are good to code!")
