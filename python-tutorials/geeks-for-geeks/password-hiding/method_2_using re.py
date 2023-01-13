# https://www.geeksforgeeks.org/password-validation-in-python/

#  importing re library (regular expressions)
import re


def main():
    # passwd = 'Geek12@' - valid
    # passwd = [try a password with less than 6 characters or more than 20 characters] - invalid
    # for example:  'asddsasdf asdfa sdfa dfasdf 22f'
    passwd = input("Password: ")
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    # compiling regex
    pattern = re.compile(reg)
    # searching regex
    match = re.search(pattern, passwd)

    # validating conditions
    if match:
        print("Password is valid.")
    else:
        print("Password invalid !!")


# Driver Code
if __name__ == '__main__':
    main()
