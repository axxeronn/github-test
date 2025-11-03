import random
import string

def generate_password(min_length=12, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_chars:
        characters += specials

    password = ''
    meet_requirement = False
    has_number = False
    has_char = False

    while (len(password) < min_length) or (numbers and not has_number) or (special_chars and not has_special):
        new_char = random.choice(characters)
        password += new_char
        if new_char in digits:
            has_number = True
        if new_char in specials:
            has_special = True

    return password

min_length = int(input("Enter minimum password length (default 12): ") or 12) 
has_number = input("Include numbers? (y/n, default y): ").lower() != 'n'
has_special = input("Include special characters? (y/n, default y): ").lower() != 'n'

password = generate_password(min_length, has_number, has_special)
print("Generated password: " + password)