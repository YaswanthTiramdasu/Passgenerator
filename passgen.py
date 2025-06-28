import random
import string

def generate_password(length=12):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation


    all_chars = lowercase + uppercase + digits + symbols

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]


    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    return ''.join(password)


if __name__ == "__main__":
    length = int(input("Enter password length (minimum 4): ") or 12)
    if length < 4:
        print("Password length must be at least 4!")
    else:
        password = generate_password(length)
        print("Generated Password:", password)