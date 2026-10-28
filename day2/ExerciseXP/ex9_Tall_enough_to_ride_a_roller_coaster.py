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