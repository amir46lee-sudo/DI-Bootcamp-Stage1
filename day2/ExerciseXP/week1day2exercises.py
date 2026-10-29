# Exercise 1: Hello World
# Instructions
# Print the following output using one line of code:
print(str("Hello World\n") * 4)

# Exercise 2: Some Math
# Instructions
# Write code that calculates the result of:
# (99^3)*8 (meaning 99 to the power of 3, times 8).
print((99**3)*8)

# Exercise 3: What is the output?
# Instructions
# Predict the output of the following code snippets:
# Coment what is your guess, then run the code and compare
5 < 3 #False
3 == 3 #True
3 == "3" #False
"3" > 3 #False
"Hello" == "hello" #False

# Exercise 4: Your computer brand
# Instructions
# Create a variable called computer_brand and assign it the name of your computer brand as a string
# Then print the following sentence using an f-string: "I have a <computer_brand> computer"
computer_brand = "dell"
print(f"I have a {computer_brand} computer")

# Exercise 5: Your information
# Instructions
# Create variables for your name, age, and favorite color
# Then print a sentence using an f-string that includes all three variables
name = "Amir"
age = 37
shoe_size = 10
info = f"My name is {name}, I am {age} years old, and my shoe size is {shoe_size}."
print(info)

# Exercise 6: A & B
# Instructions
# Create two variables, a and b.
# Each variable's value should be a number.
# If a is bigger than b, have your code print "Hello World".
a = 15
b = 10
if a > b:
    print("Hello World")

# Exercise 7: Odd or Even
# Instructions
# Write code that asks the user for a number and determines whether the number is odd or even.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Exercise 8: What's your name?
# Instructions
# Write code that asks the user for their name and then prints a funny message based on the outcome.
name = input("What is your name? ")
if name.lower() == "Amir":
    print("Hello Amir, you are an absolute legend!")
else:
    print("Bruh")

# Exercise 9: Tall enough to ride a roller coaster?
# Instructions
# Write code that asks the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.
height = int(input("What is your height in centimeters? "))
if height >= 145:
    print("You are tall enough to ride the roller coaster!")
else:
    print("You are not tall enough to ride the roller coaster.")