# Variables

account = 'Miguel' 
password = 'SuperSecret'

account2 = 'Testing'
password = 'SuperSecret'

# Functions

def getCredentials():
	# declaring local variables as global makes them global (seen outside this function, so we can send them to checkLogin)
	global enteredUser 
	global enteredPassword
	enteredUser = input("Please enter your username:")
	enteredPassword = input("Thank you " + enteredUser + ". Now please enter your password:")

def checkLogin(user, passw): 
    if (user == account) and (passw == password):
       print('Access granted')
       return True
    else:
       print('Incorrect Username or Password. \n Access denied.') 
       return False

# Check for login in a while loop that doesn't stop until checkLogin returns True.

getCredentials()
while checkLogin(enteredUser, enteredPassword) != True:
	getCredentials()  