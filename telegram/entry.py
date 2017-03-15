# -*- coding: utf8 -*-

import requests

def point(event, content):
    print(event)
    send_message(event["message"]['from']['id'], event["message"]['text'])


def send_message(chat_id, text):
    url = 'https://api.telegram.org/bot{token}/{method}'.format(
        token="354977742:AAGaPXJ2xUup0bbyf3q4GkcLoaIV6aLxVOo",
        method="sendMessage")
    data = {
        'chat_id': chat_id,
        'text': text
    }
    r = requests.post(url, data=data)
    print(r.json())

'''
def start_request():
    url = 'https://api.telegram.org/bot{token}/{method}'.format(
        token="354977742:AAGaPXJ2xUup0bbyf3q4GkcLoaIV6aLxVOo",
        method ='setWebhook' )
    data = {
        'url':'https://unbh74bw1e.execute-api.us-west-2.amazonaws.com/v0/bot_handler'
    }
    r = requests.post(url, data = data)
    print(r.json())
'''
if __name__ == '__main__':
    start_request()