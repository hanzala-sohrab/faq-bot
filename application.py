import requests
import json

from flask import Flask, request

application = Flask(__name__)


def get_rasa_response(sender, message):
    URL = "http://localhost:5005/webhooks/rest/webhook"
    headers = {"Content-Type": "application/json"}
    data = {
        "sender": sender,
        "message": message
    }
    data = json.dumps(data)
    resp = requests.post(url=URL, data=data, headers=headers)
    return resp.json()


# def send_message(whatsappNumber, messageText):
#     URL=f"{proj_setings.API_ENDPOINT}/api/v1/sendSessionMessage/{whatsappNumber}?messageText={messageText}"
    
#     headers = {"Authorization": proj_setings.ACCESS_TOKEN}

#     resp = requests.post(url=URL, headers=headers)
#     return resp.json()


@application.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    senderName = data['senderName']
    # Sending user input to Rasa server
    resp = get_rasa_response(sender=data['waId'], message=data['text'])
    text = resp[0]['text'].replace("{name}", senderName)
    # Sending response from the Rasa server back to the user
    # resp = send_message(whatsappNumber=data['waId'], messageText=text)
    return resp


if __name__ == '__main__':
    application.run(port=8000)