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



# for loops

# prints:
#     dog is a mammal
#     cat is a mammal
#     mouse is a mammal


for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))


# range(number) returns an iterable of numbers from zero up to (but excluding) the given number    
# prints:
#     0
#     1
#     2
#     3


for i in range(4):
    print(i)


# range(lower,upper) returns an iterable of numbers from zero up to (but excluding) the upper number
# prints:
#     4
#     5
#     6
#     7


for i in range(4, 8):
    print(i)


# range(lower, upper, step) returns an interable numbers from the lower number to the upper number, incrementing by the step.
# If not defined, default step is 1
# prints:
#     4
#     6


for i in range(4, 8, 2):
    print(i)


# Loop over a list to retrieve both index and value of each list item
#     0 dog
#     1 cat
#     2 mouse

animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print(i, value)


# while loops work as expected, loop until no longer true
# prints:
#     0
#     1
#     2
#     3

x = 0
while x < 4:
    print(x)
    x += 1  # Note that x++ does not work in Python because variables are pointers, not values.


