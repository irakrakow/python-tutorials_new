# https://www.youtube.com/shorts/9RQld9rGhgE

# bad practice:  password is displayed while the user is typing it in
import pwinput as pin
password = input('Try: ')
print('Password (not so good):', password)

# need to do pip install pwinput to install the library
# better practice: replace the password with asterisks
# tip to hide password when user types it in
password = pin.pwinput('Try again: ', '*')
print('Password (better):', password)
