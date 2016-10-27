#Version 1.0 stable
from content.includes.emailer import *
from content.includes.UserInterface import *
import sys
if(len(sys.argv) == 1):
	args = readUserInput()
	send_mail(args[2], args[3], args[4], readMailText())
elif(sys.argv[1] == "-h"):
	print("Malicious Mail: \n[FROM (forename, name, mailaddress), SUBJECT, RECIPIENT]")
else:
	send_mail(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5], readMailText())
		