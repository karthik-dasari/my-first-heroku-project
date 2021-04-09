from twilio.rest import Client 
 
account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 
def send_message():

    message = client.messages.create( 
                              from_='whatsapp:',  
                              body='hi',      
                              to='whatsapp:' 
                          ) 
 
    print(message.sid)

