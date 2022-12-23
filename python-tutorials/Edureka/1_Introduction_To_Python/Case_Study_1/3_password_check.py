import re

# define the password to be checked
password = input("Password: ")

# check if the password contains at least 1 lowercase letter
if not re.search(r"[a-z]", password):
    print("Password must contain at least 1 lowercase letter.")

# check if the password contains at least 1 digit
if not re.search(r"[0-9]", password):
    print("Password must contain at least 1 digit.")

# check if the password contains at least 1 uppercase letter
if not re.search(r"[A-Z]", password):
    print("Password must contain at least 1 uppercase letter.")

# check if the password contains at least 1 special character
if not re.search(r"[$#@]", password):
    print("Password must contain at least 1 special character.")

# check if the password is at least 6 characters long
if len(password) < 6:
    print("Password must be at least 6 characters long.")

# check if the password is no more than 12 characters long
if len(password) > 12:
    print("Password must be no more than 12 characters long.")
