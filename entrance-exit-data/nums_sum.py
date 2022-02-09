# Packages
import http  # Import the http package module
from http import client  # Import the module client from http package
from http.client import HTTP_PORT  # Import the constant HTTP_PORT from the client module from http package


# Virtual environment
# sudo apt install python3-venv
# python3 -m venv .venv
# source .venv/bin/activate
# which python

import random

my_number = 0
while my_number < 42:
    # Input comes as str. Change to int to sum.
    my_number += int(input("Write your number: "))
print("Your number sum is greater then 42")


# Entrance
random_number = random.randint(1, 10)  # Chose a number between 1 and 0
guess = ""

while guess != random_number:  # While the number isn't write
    guess = int(input("What's your hint? "))  # Ask the user a number

print("The lucky number was: ", guess)
