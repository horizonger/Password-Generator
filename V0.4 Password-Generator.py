#This version can take note of passwords to the csv file
# Modules.
import string
import random

# I just wanted to do it this way
# I know there are a lot of solution for this 


# Write to csv  file part
def file_write(out_file, length):
    with open("passwords.csv", "a") as pass_file:
        pass_file.write("\n")
        length_of_pass = [length]
        length_pass = ["length of password : "]
        password = ["password : "]
        n = [" "]
        pass_file.writelines(length_pass + length_of_pass + n + password + out_file)


# Read to csv file part
def file_read():
    with open("passwords.csv", "r") as file_written:
        for item in file_written:
            print(item, end=" ")


# Variables
pass_char0 = string.punctuation + string.ascii_letters + string.digits
pass_char1 = string.ascii_lowercase + string.ascii_uppercase
pass_char = pass_char0 + pass_char1

# User input part
while True:
    pass_len = input("""
(IF YOU WANNA SEE OLD PASSWORDS JUST WRITE OLD PASSWORDS) 
ENTER THE PASSWORD LENGTH
>>>> """)
    # This part create password character when input value is true
    if pass_len.isdigit():
        new_v = []
        for cycle in range(int(pass_len)):
            pass_gen = random.choice(pass_char)
            print(f"{pass_gen}", end="")
            new_v.append(pass_gen)
        print(" ")
        file_write(new_v, pass_len)

    # This part for the read old data
    elif pass_len == "old passwords".lower():
        file_read()
    elif pass_len != "old passwords".lower():
        print(f"you should write old passwords not {pass_len}")
    # This part writes incorrectly entered values to the screen
    elif not pass_len.isdigit():
        wrong_input = []
        for char in pass_len:
            if char not in string.digits:
                wrong_input.append(char)
        print(f"I need integer value and you entered this value {wrong_input}")

