#Version 1.1.1 stable - user interface for malmail


#Ask for user input
#This function returns a list in the following order
#firstnamefrom, lastnamefrom, mailfrom, mailsubject, mailto
def readUserInput():
	mailto = str(input("Send mail to: "))
	mailfrom = str(input("Send mail from: "))
	firstnamefrom = str(input("First name: "))
	lastnamefrom = str(input("Last name: "))
	mailsubject = str(input("Subject: "))

	return [firstnamefrom, lastnamefrom, mailfrom, mailsubject, mailto]

#Read Input for mail text
#To terminate and send the mail use EOF
#This function returns the user input for mail text as a String
def readMailText():
	userInput = ""
	mailText = ""
	i = 1
	#accept new user input until EOF is new input
	while (userInput != "EOF"):
		if (i == 1):
			userInput = str(input())
			if (userInput == "EOF"):
				return mailText
			mailText = mailText + userInput
			if (userInput == "EOF"):
				return mailText
			userInput = str(input())
			i = -1
		else:
			mailText = mailText + "\n" + userInput
			userInput = str(input())
	return mailText


#####test
#print(readUserInput());
#print(readMailText());
