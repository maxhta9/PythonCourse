# Multiple assignment allows us to assign multiple values at the same time
# in one line of code

# Example of normal assignment
print("Normal assignment")
name = "Max"
age = 21
smart = True

print(name)
print(age)
print(smart)

# Multiple assignment
print("\nMultiple assignment")
#"\n" represents an Enter key in output console
name, age, smart = "Bro" , 21, True

print(name)
print(age)
print(smart)

# Second example, three people are the same age
# Instead of
print("Normal assignment")
Martha = 30
Luis = 30
Peter = 30

print(Martha)
print(Luis)
print(Peter)

# We can use multiple assignment
print("\nMultiple assignment")
Martha = Luis = Peter = 30

print(Martha)
print(Luis)
print(Peter)