"""
    Chapter 3
    Control Flow and Iterables
"""

# Making a variable for example use
some_var = 5

# if statement
# Note that indentation is important in python, spaces not tabs
# 4 space indents are standard
# Prints "some_var is smaller than 10"

if some_var > 10:
    print("some_var is bigger than 10")
elif some_var < 10:     #Equivalent to "else if" in C
    print("some_var is smaller than 10")
else:
    print("some_var is 10")

# Match/Case statements were introduced in 3.10. (This is wild to me coming from C)

command = "run"

match command:
    case "run":
        print("The robot started to run")
    case "speak" | "say_hi":        # Multiple options using OR
        print("The robot said hi")
    case code if command.isdigit(): # Conditional
        print(f"The robot executes code: {code}")
    case _: # Wildcard catch all that will never fail, used like default/else
        print("Invalid command")
    
# Output: "The robot started to run"