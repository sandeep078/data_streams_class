from twilio.rest import Client

# https://www.twilio.com/console
# https://www.twilio.com/docs/quickstart/python/sms#faq


# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="xxxxxxxxx", 
    from_="+xxxxxxxxxx",
    body="Welcome to text messaging...")

print(message.sid)
