#Version 1.0 stable
import smtplib

def send_mail(firstnamefrom, lastnamefrom, sender, subject, recipient, text):

	s = smtplib.SMTP("smtp.web.de")
	s.connect("smtp.web.de",25)
	s.starttls()
	s.login("username","password") # username, password
	
	SUBJECT = subject
	TEXT	= text
	FROM 	= firstnamefrom +" "+ lastnamefrom + " <" + sender + ">"
	TO 		= recipient
	
	message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (FROM, TO, SUBJECT, TEXT)

	s.sendmail("forename last_name <username@domain.tld>",TO,message) # First name, last name, <username@domain.tld>
	s.quit()
