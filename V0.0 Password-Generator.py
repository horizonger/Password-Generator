
# modules
import string
import random


# Variables
# I just wanted to do it this way..
# I know there are a lot of solution for this variables.
pass_char0 = string.punctuation + string.ascii_letters + string.digits
pass_char1 = string.ascii_lowercase + string.ascii_uppercase
pass_char = pass_char0 + pass_char1

# user input part
while True:
    User_input = input("Choose password length: ")

    # this part create password character when input value is true
    if User_input.isdigit():
        for password_loop in range(int(User_input)):
            password_generator_variable = random.choice(pass_char)
            print(password_generator_variable, end="")
        print(" ")
    # this part writes incorrectly entered values to the screen
    elif not User_input.isdigit():
        wrong_input = []
        for wrong_input_loop in User_input:
            if wrong_input_loop not in string.digits:
                wrong_input.append(wrong_input_loop)
        print(f"I need integer value and you entered this value(s) {wrong_input}")
