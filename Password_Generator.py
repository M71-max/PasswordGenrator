import random as r

def generate_password(num):
    uper_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    lower_letter = "abcdefghijklmnopqrstuvwxyz"

    numbers = "1234567890"
    symbols = "!@#$%^&*_+=-~,./\;:><?|"
    all_letters = uper_letter + lower_letter + symbols + numbers
    password = ""
    if length > 6:
        password = "".join(r.sample(all_letters, length))
        return password


try:
    length = int(input("Enter the Max. length of the password : "))
    print("Generated Password : ",generate_password(length))
except:
    print("Enter the positive number!")
