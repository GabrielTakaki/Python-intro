# Packages
import http  # Import the http package module
from http import client  # Import the module client from http package
from http.client import HTTP_PORT  # Import the constant HTTP_PORT from the client module from http package


# Virtual environment
# sudo apt install python3-venv
# python3 -m venv .venv
# source .venv/bin/activate
# which python


my_number = 0

while my_number < 42:
    # Input comes as str. Change to int to sum.
    my_number += int(input("Write your number: "))
print("Your number sum is greater then 42")

