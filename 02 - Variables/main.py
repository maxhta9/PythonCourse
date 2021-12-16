# A variable is a container for a value
# Behaves as the value that it contains

# Declaration of a string variable
first_name = 'Max'
last_name = 'Huerta'
full_name = first_name + " " + last_name

# This line prints the data type of the variable between the parenthesis
print(type(full_name))

# You can concatenate variables with text using the '+' symbol
print("Hello, my name is " + full_name)

# Integer variables, do not use " ".
age = 22

# Operations with integer
age = age + 1
# You can also use age += 1

# This line prints the data type of the variable between the parenthesis
print(type(age))

# You can not concatenate integer variables. You have to transform it to string variable
print("I am " + str(age))

# Float variables
height = 250.5

# This line prints the data type of the variable between the parenthesis
print(type(height))

# You have to transorm it to string variable like an integer value to concatenate strings
print("My height is " + str(height))

# Boolean variables, only store True or False
human = True

# This line prints the data type of the variable between the parenthesis
print(type(human))

# You have to transorm it to string variable like an integer value to concatenate strings
print("Are you a human? " + str(human))

