import smtplib

# app passwords:
# https://myaccount.google.com/security?utm_source=OGB&utm_medium=act#signin
# https://support.google.com/accounts/answer/185833
# 
# SMTP:
# https://support.google.com/a/answer/176600?hl=en
# http://www.geeksforgeeks.org/send-mail-gmail-account-using-python/
# 

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login('your_email@gmail.com','xxxxxx')

message = "Something is going on you need to know about."

s.sendmail("your_email@gmail.com","user_to@xyz.com",message)

s.quit()
