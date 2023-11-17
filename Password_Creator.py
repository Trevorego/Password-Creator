import random
import string
def generate_strong_password(length, numberchar, specialchar):
    password = ""
    chars = string.ascii_letters
    if (specialchar):
        chars += "".join(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ';', ':', ',', '<', '>', '.', '?', '/'])
    if (numberchar):
        chars += "0123456789"
    
    for i in range(length):
        password += random.choice(chars)
    
    return password
    
def main():
    print(generate_strong_password(16, True, True))
    
if __name__ == "__main__":
    main()