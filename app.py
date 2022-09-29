import os
from dotenv import load_dotenv
from twilio.rest import Client
from pymongo import MongoClient
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

load_dotenv()

app = Flask(__name__)
client = Client()

# Creating MongoDB connection
CONNECTION_STRING = os.environ['MONGODB_CONNECTION']
client_DB = MongoClient(CONNECTION_STRING)

@app.route('/api/whatsapp-reply', methods=['POST'])
def sendMessage():
    
    # Getting Text Message received on whatsapp
    message = request.form.get('Body', None) 
    db_name = client_DB['Whatsapp_API']

    # DB collection name
    collection_name = db_name["whatsapp_msg"] 
    data = {
        "message": message,
        "sender": request.form.get('From')
    }

    # Inserting data to DB
    collection_name.insert_one(data) 
    if message:
        msg_text = f"Hello! Thanks for the message, we will revert back to you shortly!"
        response = MessagingResponse()
        response.message(msg_text) 

        #Sending return message on whatsapp
        return str(response)

if __name__ == "__main__":
    app.run()