#Version 1.1.1 stable
version = """1.1.1 - stable
Thank you for using our tool! psittacus & splix @k4cg"""

from content.includes.emailer import *
from content.includes.UserInterface import *
import sys

#help screen
helptext = """Usage: python malmailer.py [parameters]
	or: python malmailer.py [first name, last name, sender mailaddress, subject, recipient]
	or: python malmailer.py
Send an email from a specified email (you can choose).

End email text with 'EOF'

If you are having problems sending an email you probably forgot to change the file in /content/includes/emailer.py (for more information see README.md)

Parameters are:
	-h			display this help and exit
	--help		same as -h
	--version	output version infromation and exit

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

Thank you for using our tool! psittacus & splix @k4cg"""

#Checks the length of the command line paramters, if none given use readUserInput() function from UserInterface.py
#also uses readMailText() from UserInterface.py as mailtextreader
if(len(sys.argv) == 1): #use readUserInput() as input 
	args = ["","","","","",""]
	args = readUserInput()
	send_mail(args[0], args[1], args[2], args[3], args[4], readMailText())
elif(sys.argv[1] == "-h" or sys.argv[1] == "--help" ): #user called help functionality
	print(helptext)
elif(sys.argv[1] == "--version" ): #print version infromation
	print(version)
elif(len(sys.argv) == 6): #use command line parameters
	send_mail(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5], readMailText())
else: # print help function
	print(helptext)
