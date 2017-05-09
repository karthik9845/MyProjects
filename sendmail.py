import smtplib
try:
	smtpObj=smtplib.SMTP('smtp.gmail.com',587)
	smtpObj.ehlo()
	smtpObj.starttls()

except:
	smtpObj=smtplib.SMTP_SSL('smtp.gmail.com',465)
	smtpObj.ehlo()


smtpObj.login('my_email_id@gmail.com','my_password')

smtpObj.sendmail('my_email_id@gmail.com','sender_email_id@yahoo.com','Subject: Hello, there')
smtpObj.quit()