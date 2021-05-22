from twilio.rest import Client


account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(from='', body='', to='')

print(message.sid)