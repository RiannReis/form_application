import string, random


random_str = string.ascii_letters + string.digits +string.ascii_uppercase
key = ''.join(random.choice(random_str) for i in range(12))

SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'

SECRET_KEY = key