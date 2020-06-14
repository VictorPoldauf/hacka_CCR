from flask import Flask, request , render_template,url_for
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


from  controller import *

if __name__ == "__main__":
    app.run(debug=True,port=8080)