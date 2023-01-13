# importing re library
import re

def main():
	passwd = 'Geek12@'
	reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
	
	# compiling regex
	pattern = re.compile(reg)
	
	# searching regex				
	mat = re.search(pattern, passwd)
	
	# validating conditions
	if mat:
		print("Password is valid.")
	else:
		print("Password invalid !!")

# Driver Code	
if __name__ == '__main__':
	main()
