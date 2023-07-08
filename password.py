import string
import random
def create_password(length):
    symbols=string.ascii_uppercase+string.ascii_lowercase+string.digits
    password="".join(random.sample(symbols,length))
    with open("passwords.txt", "a") as file:
        file.write(f"length={length}, password={password};\n")
        file.close()
    return password
