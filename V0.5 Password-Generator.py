#This version can take note of passwords to the text file
# modules.
import string
import random


# I just wanted to do it this way.
# I know there are a lot of solution for this


# write to csv  file part
def file_write(out_file, name):
    with open("passwords.txt", "a") as pass_file:
        pass_file.write("\n")
        password = ["password : "]
        n = " "
        pass_file.writelines(name + n)
        pass_file.writelines(password + out_file)
#This version can take note of passwords to the text file
        
        
# Variables
pass_char0 = string.punctuation + string.ascii_letters + string.digits
pass_char1 = string.ascii_lowercase + string.ascii_uppercase
pass_char = pass_char0 + pass_char1

# user input part
while True:
    print("""
     
PLEASE FIRST WRITE "where do you want to use this password "
""")
    reason = str(input(">>>>"))
    print("""
now  enter the password length    
""")
    pass_len = input(">>>>")
    # this part create password character when input value is true
    if pass_len.isdigit():
        new_v = []
        for cycle in range(int(pass_len)):
            pass_gen = random.choice(pass_char)
            print(f"{pass_gen}", end="")
            new_v.append(pass_gen)
        print(" ")
        file_write(new_v, reason)
    # this part writes incorrectly entered values to the screen
    elif not pass_len.isdigit():
        wrong_input = []
        for char in pass_len:
            if char not in string.digits:
                wrong_input.append(char)
        print(f"I need integer value and you entered this value {wrong_input}")
