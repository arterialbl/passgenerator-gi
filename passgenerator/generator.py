import random
import string

def generate_password(number_of_symbols=12):
    password = ""
    for i in range(number_of_symbols):
        randnum = random.randint(1, 4)
        
        if randnum == 1:
            password += random.choice(string.ascii_uppercase)
        elif randnum == 2:
            password += random.choice(string.ascii_lowercase)
        elif randnum == 3:
            password += random.choice(string.digits)
        else:
            password += random.choice("!_-?")
            
    return password

if __name__ == "__main__":
    print("Запущен модуль")
    print(generate_password())
