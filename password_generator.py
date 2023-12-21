import random
import string

def password_generator(password_length):
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.sample(characters, password_length))
    return password