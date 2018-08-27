"""
Project Requirements: Complete this method.
Input:
	password: A string that may need to be stripped of whitespaces.
	f: A file that serves as the dictionary.
Output: True if the password was found in the dictionary.
			False if not.

Helpful functions:
	password.strip() returns a string that is the same as password, but stripped of whitespaces at the ends.
	for instance, if password is "  i am laura   " password.strip() is "i am laura"
	This works for any variable that is a string. You need to strip the word from the dictionary as well as the password!
	if myfile is the variable that represents the file we're reading from, we can iterate through the file line by line like this:
	for line in myfile:
		print(line)
	If the myfile's contents are
		hello
		world
	on the first iteration, line would be "hello\n". on the second iteration, line would be "world\n"
	"\n" is a character that means new line. It's essentially the same as hitting enter when you type, or when you used <br> in html
"""
def password_in_dictionary(password, f):
 	for line in f:
 		passwordStripped = password.strip()
 		lineStripped = line.strip()
 		if passwordStripped == lineStripped:
 			return True
 	return False
'''
 	currentline = False
 	for line in f:
 		passwordStripped = password.strip()
 		lineStripped = line.strip()
 		if passwordStripped == lineStripped:
 			currentline = True
 	if currentline == True:
 		return True
 	else:
 		return False
'''

def compound_in_dictionary(password,f):
	newPassword = line + line
	if password == newPassword:
		return True


def main():
  f = open("dictionary.txt","r") #this line
  print("Can your password survive a dictionary attack?")
  test_password = input("Type in a trial password: ")
  if password_in_dictionary(test_password, f) or compound_in_dictionary(test_password, f):
    print("Your password was guessed in a dictionary attack.")
  else:
    print("Your pasword was NOT guessed in a dictionary attack.")
  f.close()



if __name__ == '__main__':

  main()
