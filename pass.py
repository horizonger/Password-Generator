#modules
import string
import random

#variable
pass_char = string.punctuation + string.printable

while True:
     pass_len = input("Choose password length: ") #user chooses password size in this section

    if pass_len.isdigit():
        for cycle in range(int(pass_len)):
            pass_gen = random.choice(pass_char)
            print(pass_gen, end="")
        print(" ")
    elif not pass_len.isdigit():
        wrong_input = []
        for char in pass_len:
            if char not in string.digits:
                wrong_input.append(char)
        print(f"I need integer value and you entered this value {wrong_input}")
