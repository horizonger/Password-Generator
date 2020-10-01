# This version writes data to txt file.
# modules
import string
import random
import csv


# write to csv  file part
def file_write(out_file, num):
    with open("passwords.csv", "a") as pass_file:

        pass_file.write("\n")
        user_id_number = [num]
        n = [" "]
        pass_file.writelines(user_id_number + n + out_file)


# read to file part
def file_read():
    with open("passwords.txt", "r") as file_written:
        for item in file_written:
            print(item, end=" ")


# Variables
pass_char0 = string.punctuation + string.ascii_letters + string.digits
pass_char1 = string.ascii_lowercase + string.ascii_uppercase
pass_char = pass_char0 + pass_char1

# user input part
while True:
    pass_len = input("""
(IF YOU WANNA SEE OLD PASSWORDS JUST WRITE OLD PASSWORDS) 
ENTER THE PASSWORD LENGTH
>>>> """)
    # this part create password character when input value is true
    if pass_len.isdigit():
        new_v = []
        for cycle in range(int(pass_len)):
            pass_gen = random.choice(pass_char)
            print(f"{pass_gen}", end="")
            new_v.append(pass_gen)
        print(" ")
        file_write(new_v, pass_len)

    # this part for the read old data
    elif pass_len == "old passwords".lower():
        file_read()
    # this part writes incorrectly entered values to the screen
    elif not pass_len.isdigit():
        wrong_input = []
        for char in pass_len:
            if char not in string.digits:
                wrong_input.append(char)
        print(f"I need integer value and you entered this value {wrong_input}")
