"""
    Chapter 2
    Variables and Collections
"""

# Print Function
print("Hello world")

# Print generally ends the line with \n. If you want it to end with something else, add the end="" argument
print("Hello World", end="!")
print("test")   # Note that this is not on a new line because I didn't add \n to the last print in the end argument

# To grab input from the command line (Like scanf() in C)
input_string_var = input("Enter some data: ")   # Will put in stdout "Enter some data: " then anything typed after will be assigned to input_string_var
print(input_string_var)

# Only assignments, no declarations. Assign values/type to variables. 
# Note that variables are conventionally snake_case

example_variable = 7

# The following line will error out because it is declared not assigned. 
# example_variable_2

# Referencing a variable that has not yet been assigned will also raise an error. 

# if is the equivalent to C's ? operator. 

result = "yay" if 0 > 1 else "nay"
print(result)   # Prints nay

# Python doesn't have arrays that i'm used to. Python uses lists. The biggest difference between lists and arrays is that lists do not need the same datatype for the entire set.
# A list can have mixed ints, strings, floats, etc. 
# Unlike something like an array, lists are actually OBJECTS. They have some built in functions shown below. 

# Lists can be initialized blank or prefilled. 
blank_li = []
prepop_li = [4,5,6]

blank_li.append(1)  # blank_li is now [1]
blank_li.append(2)  # blank_li is now [1,2]
blank_li.append(4)  # blank_li is now [1,2,4]
blank_li.append(3)  # blank_li is now [1,2,4,3]

blank_li.pop()      # Works as you'd expect, blank_li is now [1,2,4]

blank_li.append(3)  # Putting the value back, now [1,2,4,3]

# Indexing works as expected with a fun little shortcut to the last variable
blank_li[0]     # Returns first index, 1
blank_li[-1]    # Returns LAST index, 3

# Looking out of bounds will raise an error. Line is commented out to maintain runability. 
# blank_li[4]   # Error due to out of bounds

# We can also range indexing
blank_li[1:3]   # Return list from index 1 to 3, [2,4]
blank_li[2:]    # Return list starting at 2 until the end, [4,3]
blank_li[:3]    # Return list from 0 to 3, [1,2,4]
blank_li[::2]   # Return list selecting indexes with a step size of 2 (every other), [1,4]
blank_li[::-1]  # Return list in reverse order, [3,4,2,1]
# Combinations also work
# blank_li[start:end:step]


# Copying lists makes some fun stuff happen
li1 = blank_li      # li1 and blank_li reference the same object
li2 = blank_li[:]   # li2 and blank_li have copied contents, but are completely different objects. (li2 is blank_li will return false)

# del will delete an index from a list
del blank_li[2]     # blank_li is now [1,2,3]

# .remove will remove the first occurance of a value
blank_li.remove(2)  # blank_li is now [1,3]
#blank_li.remove(2) # errors out because there is no 2 in the list

# We can insert elements at indexes
blank_li.insert(1,2)    # Inserts 2 before index 1, [1,2,3] again

# We can parse the list for a value
blank_li.index(2)   # Returns the index that 2 is located at, 1
blank_li.index(4)   # Error due to 4 not being in the list currently

# Lists can be added
blank_li + prepop_li # [1,2,3,4,5,6] Note that the values for blank_li and prepop_li are not modified. Could assign these to a new list. 

# If we want the values to be added to eachother
blank_li.extend(prepop_li)  # blank_li is now [1,2,3,4,5,6]

# Check for existance in a list
1 in blank_li   # True

# Len also works
len(blank_li)   # 6





# Tuples are like lists but immutable. The tuples themselves are immutable, but the items they're pointing at can be. 
# Ints, str, and tuples inside of a tuple is immutable, but lists, dicts, and sets can be edited as long as it's always refering to the same one. 

tup = (1,2,3)
tup[0]  # 1

# This will not work because incrementing in python makes the variable change pointer destination which is not allowed for immutable objects like tuples
# tup[0] = 5

# Tuples have to have a comma after the 0th index if len = 1 or it will not register as a tuple. Only applies to len = 1
type((1))   # Class 'int'
type((1,))  # Class 'tuple'
type(())    # Class 'tuple'

# Most list operators work on tuples, just not ones that would be stopped by immutability
len(tup)         # 3
tup + (4, 5, 6)  # (1, 2, 3, 4, 5, 6)
tup[:2]          # (1, 2)
2 in tup         # True

# Lists and Tuples can be unpacked into variables
a, b, c = (1, 2, 3)     # a = 1, b = 2, c = 3
# Unpacking can also be extended
a, *b, c = (1, 2, 3, 4) # a = 1, b = [2, 3], c = 4
# Tuples are created by default if you leave out parentheses
d, e, f = 4, 5, 6       # Tuple 4, 5, 6 is unpacked onto d, e, f (d = 4, e = 5, f = 6)
# Variable Swapping
d, e = e, d             # d = 5 and e = 4

