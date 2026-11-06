# Exercise 1: Favorite Numbers
# Key Python Topics:
# Sets
# Adding/removing items in a set
# Set concatenation (using union)
# Instructions:
# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.
my_fav_numbers = {3, 8, 7, 24}
first_new_num = 64
last_new_num = 85
my_fav_numbers.add(first_new_num)
my_fav_numbers.add(last_new_num)
my_fav_numbers.remove(last_new_num)
print(my_fav_numbers)
friend_fav_numbers = {26, 34, 33, 55}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# Exercise 2: Tuple
# Key Python Topics:
# Tuples (immutability)
# Instructions:
#Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.
my_tuple = (3, 8, 10, 5)
print(my_tuple[0])  # Accessing the first element of the tuple
my_tuple += (12,)  # Attempting to add an integer to the tuple
print(my_tuple)  # Printing the updated tuple
#my_tuple.append(15)
#print(my_tuple)  # Raise an AttributeError since tuples do not have an append method

# Exercise 3: List Manipulation
# Key Python Topics:
# Lists
# List methods: append, remove, insert, count, clear
# Instructions:
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("kiwi")
print(basket)
basket.insert(0, "Apples")
print(basket)
apple_count = basket.count("Apples")
print(f"Apples appear {apple_count} times in the list.")
basket.clear()
print(basket)  # Printing the final state of the list, which should be empty

# Exercise 4: Floats
# Key Python Topics:
# Lists
# Floats and integers
# Range generation
# Instructions:
# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?
mixed_types = [step / 2 for step in range(3, 11)]  # Generates the sequence from 1.5 to 5.0
print(mixed_types)  # Printing the list of mixed types

# Exercise 5: For Loop
# Key Python Topics:
# Loops (for)
# Range and indexing
# Instructions:
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.
all_numbers = list(range(1, 21))
print(all_numbers)  # Printing all numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i) # Printing even numbers from 1 to 20

# Exercise 6: While Loop
# Key Python Topics:
# Loops (while)
# Conditionals
# Instructions:
# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop
while True:
    name = input("Please enter your name: ")
    if not name.isalpha() or len(name) < 3:
        print("Invalid input. Please enter a valid name")
    else:
        print("Thank you!")
        break

# Exercise 7: Favorite Fruits
# Key Python Topics:
## Input/output
# Strings and lists
# Conditionals
# Instructions:
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"
favorite_fruits = input("Please enter your favorite fruits (separated by spaces): ").split()
fruit_choice = input("Please enter the name of any fruit: ")
if fruit_choice in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# Exercise 8: Pizza Toppings
# Key Python Topics:
# Loops
# Lists
# String formatting
# Instructions:
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.
toppings = []
while True:
    topping = input("Please enter a pizza topping (or type 'quit' to finish): ")
    if topping == 'quit':
        break
    
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")
total_cost = 10 + len(toppings) * 2.50

print(f"Total cost of the pizza with {len(toppings)} toppings: ${total_cost:.2f}")
print(f"Toppings: {','.join(toppings)}")

# Exercise 9: Cinemax Tickets
# Key Python Topics:
# Conditionals
# Lists
# Loops
# Instructions:
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.
person = []
prices = []
while True:
        age_input = input("enter the person's age (or type 'done' to finish): ")
        if age_input.lower() == 'done':
            if prices:
                total_cost = sum(prices)
                print(f"Total ticket cost: ${total_cost:.2f}")
            break
        try:
            age = int(age_input)
            person.append(age)

            if age < 3:
                print("You are free to enter.")
            elif 3 <= age <= 12:
                prices.append(10)
                print("ticket costs $10.")
            else:
                prices.append(15)
                print("ticket costs $15.")
        
        except ValueError:
            print("Invalid input. Please enter a valid age or 'done' to finish.")

# Bonus:
# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.
attendees = []
while True:
    age_input = input("Enter the age of the attendee (or type 'done'): ")
    if age_input.lower() == 'done':
        break
    try:
        age = int(age_input)
        if age >= 16 and age <= 21:
            attendees.append(age)
        else:
            print("not allowed to watch this movie,")
    except ValueError:
        print("Invalid input. Please enter a valid age or 'done' to finish.")
print(f"final list of attendees: {attendees}")

