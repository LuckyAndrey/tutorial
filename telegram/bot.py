# https://api.telegram.org/bot356600671:AAGylsvErcp7DCNIap39K84-1L-8oborby0/sendMessage?chat_id=371744096&text=hi
# https://api.telegram.org/bot356600671:AAGylsvErcp7DCNIap39K84-1L-8oborby0/getupdates
# https://api.telegram.org/bot356600671:AAGylsvErcp7DCNIap39K84-1L-8oborby0/getpdates

import requests
from telegram import mics
from telegram import bitcoin as btc
import json
global update_id_last
update_id_last = 0


URL ='https://api.telegram.org/bot'+mics.token+'/'
# token = '354977742:AAGaPXJ2xUup0bbyf3q4GkcLoaIV6aLxVOo'

def get_updates():
    url = URL + 'getupdates'
    print(url)
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text  = data['result'][-1]['message']['text']
    last_obj = data['result'][-1]
    current_update_id = last_obj['update_id']
    global update_id_last

    if update_id_last != current_update_id:
        message = {'chat_id': chat_id,
                   'message_text': message_text}
        update_id_last = current_update_id
        return message
    else:
        return None

def send_message(chat_id, text = "Please wait"):
    url = URL+'sendmessage?chat_id={}&text={}'.format(chat_id,text)
    requests.get(url)

while True:
    try:
        answer = get_message()
        print(answer)
        chatid = answer['chat_id']
        text = answer['message_text']
        if text == '/btc':
            send_message(chatid,btc.get_btc())
    except:
        continue

# with open('updates.json', 'w') as f:
#     json.dump(d, f, indent=3,ensure_ascii=False)