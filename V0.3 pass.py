import string
import random


def file_write(out_file):
    with open("passwords.txt", "a") as pass_file:
        pass_file.write("\n")
        pass_file.writelines(out_file)


def file_read():
    with open("passwords.txt", "r") as file_written:
        for item in file_written:
            print(item, end=" ")


pass_char0 = string.punctuation + string.ascii_letters + string.digits
pass_char1 = string.ascii_lowercase + string.ascii_uppercase
pass_char = pass_char0 + pass_char1

while True:
    pass_len = input("""
(IF YOU WANNA SEE OLD PASSWORDS JUST WRITE OLD PASSWORD) 
ENTER THE PASSWORD LENGTH
>>>>
""")

    if pass_len.isdigit():
        new_v = []
        for cycle in range(int(pass_len)):
            pass_gen = random.choice(pass_char)
            print(f"{pass_gen}", end="")
            new_v.append(pass_gen)
        print(" ")
        file_write(new_v)
    elif pass_len == "old password".lower():
        file_read()
    elif not pass_len.isdigit():
        wrong_input = []
        for char in pass_len:
            if char not in string.digits:
                wrong_input.append(char)
        print(f"I need integer value and you entered this value {wrong_input}")
