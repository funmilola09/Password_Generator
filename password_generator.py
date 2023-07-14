import secrets
import string


def create_PW(pw_length=12):
    letters = string.ascii_letters
    digits = string.digits
    special_char = string.punctuation

    alphabet = letters + digits + special_char
    pwd = ''
    pw_strong = False

    while not pw_strong:
        pwd = ''
        for i in range(pw_length):
            pwd += ''.join(secrets.choice(alphabet))

        if (any(char in  special_char for char in pwd) and
            sum(char in digits for char in pwd) >= 2):
            pw_strong = True

        return pwd

if __name__ == '__main__':
    print(create_PW())
