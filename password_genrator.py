import string
import random

# Password generator function
def pass_gen(length=12, uppercase_letters=True, lowercase_letters=True, special_letters=True, digits=True):
    characters = ''
    
    if uppercase_letters:
        characters += string.ascii_uppercase
    
    if lowercase_letters:
        characters += string.ascii_lowercase

    if special_letters:
        characters += string.punctuation

    if digits:
        characters += string.digits
    
    if not characters:
        print("Error: Must select at least one character type")
        return None
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password  # Return the generated password

# Get user input
pass_length = int(input("Enter length for password: "))
include_uppercase = input("Would you like to include uppercase characters? (y/n): ").lower() == 'y'
include_lowercase = input("Would you like to include lowercase characters? (y/n): ").lower() == 'y'
include_special = input("Would you like to include special characters? (y/n): ").lower() == 'y'
include_digit = input("Would you like to include digits? (y/n): ").lower() == 'y'

# Call the password generator
passwd = pass_gen(
    length=pass_length,
    uppercase_letters=include_uppercase,
    lowercase_letters=include_lowercase,
    special_letters=include_special,
    digits=include_digit
)

# Output the generated password
if passwd:
    print("Generated password:", passwd)
else:
    print("Can't generate password")