# Type casting let us convert data from one data type to another

x = 1 # integer value
y = 2.0 # float value
z = "3" # string value

print(x)
print(y)
print(z)

# If we want to redefine the variable into a different data type
x = float(x)


# Type casting applied to the predefined variables temporarily
print("\nType casting: ")
print(x)
print(int(y))

# If we print 'z', it will function as a string
print("\n" + z * 3)
# After we redefined it, it will do the corresponding math
z = float(z)
print(z * 3)

# We can not print integer or float values with in a string in the same print, so we use type casting to convert
# the variable into a string
print("\nX is float: " + str(x))