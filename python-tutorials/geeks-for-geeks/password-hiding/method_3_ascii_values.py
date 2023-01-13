# https://www.geeksforgeeks.org/password-validation-in-python/
#This code is contributed by Edula Vinay Kumar Reddy

def password_check(passwd):
	SpecialSym =['$', '@', '#', '%']
	val = True
	if len(passwd) < 6:
		print('length should be at least 6')
		val = False
	if len(passwd) > 20:
		print('length should be not be greater than 8')
		val = False

	# Check if password contains at least one digit, uppercase letter, lowercase letter, and special symbol
	has_digit = False
	has_upper = False
	has_lower = False
	has_sym = False
	for char in passwd:
		if ord(char) >= 48 and ord(char) <= 57:
			has_digit = True
		elif ord(char) >= 65 and ord(char) <= 90:
			has_upper = True
		elif ord(char) >= 97 and ord(char) <= 122:
			has_lower = True
		elif char in SpecialSym:
			has_sym = True

	if not has_digit:
		print('Password should have at least one numeral')
		val = False
	if not has_upper:
		print('Password should have at least one uppercase letter')
		val = False
	if not has_lower:
		print('Password should have at least one lowercase letter')
		val = False
	if not has_sym:
		print('Password should have at least one of the symbols $@#')
		val = False

	return val
print(password_check('Geek12@')) # should return True
print(password_check('asd123')) # should return False
print(password_check('HELLOworld')) # should return False
print(password_check('helloWORLD123@')) # should return True
print(password_check('HelloWORLD123')) # should return False
#This code is contributed by Edula Vinay Kumar Reddy
