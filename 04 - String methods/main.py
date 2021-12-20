# String methods
name = "Max"

#The method len() return the length of the given string
print("\nlen() method:")
print(len(name))

# If we put a "." after the variable, we can use different methods, for example
# The method find() returns the index position of a letter, if the letter is not found, returns -1
print("\nfind() method:")
print(name.find("B"))
print(name.find("a"))

# This method capitalize the first letter of the variable
example = "\nnot capitalized"
print("capitalize() method:")
print(example.capitalize())

# This method upper case the string
example = "hello"
print("\nupper() and lower() method:")
print(example.upper())

# And the counterpart is lower
print(example.lower())

# The next method returns true or false if the string is full of digits or not
# This method returns true if the string is full of digits only
print("\nisdigit() method:")
print(example.isdigit())
example = "131513"
print(example.isdigit())

# The counterpart method returns true or false if the string is full of alphabetial letters
# If the string contains an space, it will return false
example = "helloworld"
print("\nisalpha() method:")
print(example.isalpha())
example = "131412"
print(example.isalpha())

# This method returns the number of times a given string is contained inside a variable
example = "Hello World"
print("\ncount() method")
print(example.count("o"))
print(example.count("or"))
print(example.count("c"))

# With this method we can replace characters, it needs 2 arguments, the character we will replace and
# the character that we will replace our character with
print("\nreplace() method:")
print(example.replace("o", "a"))

# We can display a string multiple times by multipling it by a number
print(example*3)

