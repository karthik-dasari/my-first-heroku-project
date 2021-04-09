from twilio.rest import Client 
 
account_sid = 'AC48a591cb952123ed25f2256c870e1c9b' 
auth_token = 'c2d4be1f8b14fea8d10c2c356f875246' 
client = Client(account_sid, auth_token) 
def send_message():

    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='hi',      
                              to='whatsapp:+917702329668' 
                          ) 
 
    print(message.sid)

