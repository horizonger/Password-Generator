import string
import random
import xlsxwriter


def file(out_file):
    out_x = xlsxwriter.Workbook("password.xlsx")
    pass_w = out_x.add_worksheet()
    pass_w.write("A1", "Passwords")
    pass_w.write("A2", str(out_file))
    out_x.close()


pass_char0 = string.punctuation + string.ascii_letters + string.digits
pass_char1 = string.ascii_lowercase + string.ascii_uppercase
pass_char = pass_char0 + pass_char1

pass_len = input("Choose password length: ")

if pass_len.isdigit():
    new_v = []
    for cycle in range(int(pass_len)):
        pass_gen = random.choice(pass_char)
        print(pass_gen, end="")
        new_v.append(pass_gen)
    print(" ")
    file(new_v)
elif not pass_len.isdigit():
    wrong_input = []
    for char in pass_len:
        if char not in string.digits:
            wrong_input.append(char)
    print(f"I need integer value and you entered this value {wrong_input}")
    
