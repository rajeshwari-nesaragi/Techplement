import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_length = 8
random_password = generate_password(password_length)
print("Random password:", random_password)