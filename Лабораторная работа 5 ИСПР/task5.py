from random import sample
from string import ascii_uppercase, ascii_lowercase, digits


def get_random_password(n=8) -> str:
    return ''.join(sample(ascii_uppercase + ascii_lowercase + digits, n))


print(get_random_password())
