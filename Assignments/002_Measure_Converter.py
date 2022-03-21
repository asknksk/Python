"""
Task-1:

Write a short Python program that asks the user to enter Celsius temperature (it can be a decimal number), converts the entered temperature into Fahrenheit degree and prints the result.

Task-2:
Write a short Python program that asks the user to enter a distance (it can be a decimal number) in kilometers, converts the entered distance into miles and prints the result.
"""

celsius = float(input("Please enter to Celsius temperature : "))

kilometer = float(input("Please enter to kilometer distance : "))

fahrenheit = (celsius * 1.8) + 32

mile = kilometer * 0.621371192

print(f"Your Fahrenheit degree {fahrenheit} fahrenheit.")

print(f"Your mile distance {mile} miles.")