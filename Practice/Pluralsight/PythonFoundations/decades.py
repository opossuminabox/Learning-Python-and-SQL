# Jacob Turcotte
# Program is to ask the user their age, then respond with how many decades + years they've lived. 

print("How old are you?")
age = int(input("Your Age: "))

# Floor Division to get decades, Modulo for remaining age in years
decades = age // 10
years = age % 10

print(f"You are {decades} decades old and {years} years old.")