"""Basic function exercises."""
import math


def print_hello():
    print("Hello")
    # code here


def get_hello() -> str:
    return "Hello"


def ask_name_and_greet_user():
    name = input("Please enter your name \n")

    if name.lower() == "thanos":
        print("Get out of here, Thnos! Nobody wants to play with you!")
    else:
        print("Hi, ", name, ". Would you like to have a Hamburger?")

def calculate_hypotenuse_length(a, c) -> float:
    return math.hypot(a, c)
    # code here

def calculate_cathetus_length(a, c) -> float:
    """Return cathetus value."""
    # code here


if __name__ == '__main__':
    print_hello()  # should print "Hello"
    hello = get_hello()  # should return "Hello"
    print(hello)  # let's check the value of hello variable
    ask_name_and_greet_user()  # should ask name and greet
    print(calculate_hypotenuse_length(3, 4))  # should print 5.0
    print(calculate_cathetus_length(3, 5))  # should print 4.0