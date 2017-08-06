from django.shortcuts import render
from django.http import HttpResponse
import os

from .sdk.models import *

def index(request):
    return HttpResponse("Hello Heroku!!")

import json
def webhook(request):
    request_json = json.loads(request.body.decode('utf-8'))
    for e in request_json['events']:
        reply_token = e['replyToken']
        message_type = e['message']['type']


        if message_type == 'text':
            text = e['message']['text']
            reply_text(reply_token, str(request_json['events'][0]))
        else:
            reply_text(reply_token, str(request_json['events'][0]))
    return HttpResponse(request_json['events'])


import random
import requests

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', 3)
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}


def reply_text(reply_token, text):
    messages = [TextSendMessage(text=text)]
    
    payload = {
          "replyToken":reply_token,
          "messages": [message.as_json_dict() for message in messages]
    }

    requests.post(REPLY_ENDPOINT, headers=HEADER, data=json.dumps(payload))
