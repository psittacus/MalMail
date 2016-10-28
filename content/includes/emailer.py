#Version 1.1 stable
import smtplib

#This function sends an email with the sepcified paramters via the server specified in the function
def send_mail(firstnamefrom, lastnamefrom, sender, subject, recipient, text):

	s = smtplib.SMTP("smtp.web.de") #server name
	s.connect("smtp.web.de",25)
	s.starttls()
	s.login("username","password") # CHANGE !!!! (your) username, password
	
	SUBJECT = subject
	TEXT	= text
	FROM 	= firstnamefrom +" "+ lastnamefrom + " <" + sender + ">"
	TO 		= recipient
	
	message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (FROM, TO, SUBJECT, TEXT)

	s.sendmail("firstname lastname usernmae@web.de",TO,message) # CHANGE !!!! (your) First name, last name, <username@domain.tld>
	s.quit()
