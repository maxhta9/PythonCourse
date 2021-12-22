# We can input data from the users by using the function input()
# Inside the function we can display text to let the user know what data we want to collect
#input("What is your name?: ")

# We can also save the input data to a variable using the next syntax

name = input("What is your name?: ")

# It is important to know that the input function receives an string, so
# if we want to save a number, we have to type cast the function.
# If the user insert a float number, the type cast will not work correctly and end up in an error
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))
print("Hello, " + name + " you are " + str(age) + " old!")
print("You are " + str(height) + " cm tall")
