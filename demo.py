import string
import secrets


def password_generator (length= 10):
    # creating a variable to hold alphabet and numbers to generate into a password.
    characters = string.ascii_letters + string.digits + string.punctuation
    # returns random password with a mixture of characters
    return ''.join(secrets.choice(characters) for i in range(length))

# to output the password

password = password_generator()
print(f"Here is your new password: {password}")