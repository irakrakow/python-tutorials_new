# https://www.youtube.com/watch?v=dgBCEB2jVU0
# http://arjancodes/designguide
# why Arjan likes type hints
# Python is dynamically typed.  Python figures out the type when the variable, return type, etc. is declared.
# type hints
# interpreter ignores type hints, so what's the purpose?
# instead of type hints, one could create unit tests to test the types
# benefits:
# provides documentation of what the type should be
# types are useful when coding in IDE
# types make coupling more explicit. Can know what modules are expected.  See beautiful_soup
# type hints forces you to define the data structures can simplify code.
# Procedure:  specify the type hints, when error occurs, see what expected types are, fix accordingly.
# adds an extra layer of simplicity and accuracy

def luhn_checksum(number: str) -> bool:
    '''
    Check that the provided number passes the Luhn checksum algorithm
    For more information, see https://en.wikipedia.org/wiki/Luhn_algorithm.

            Parameters:
                number (str): a number represented by a string.

            Returns:
                luhn_checksum (bool): True if Luhn checksum is correct, false otherwise
    '''
    def digits_of(nr: str) -> list[int]:
        return [int(d) for d in nr]

    digits = digits_of(number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for digit in even_digits:
        checksum += sum(digits_of(str(digit*2)))
    return checksum % 10 == 0


a_number = luhn_checksum("123456")
print(int(a_number))
