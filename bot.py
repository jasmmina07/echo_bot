import requests
from settings import *
from time import sleep
from sends import *

last_update_id=""
while True:
    update=(requests.get(url+"/getUpdates")).json()
    update_id=update["result"][-1]["update_id"]
    if update_id!=last_update_id:
        last_update_id=update_id
        if update["result"][-1]["message"].get("text",False):
            chat_id=update["result"][-1]["message"]["chat"]["id"]
            text=update["result"][-1]["message"]["text"]
            send_message(chat_id,text)
        elif update["result"][-1]["message"].get("photo",False):
            chat_id=update["result"][-1]["message"]["chat"]["id"]
            photo=update["result"][-1]["message"]["photo"][-1]["file_id"]
            send_photo(chat_id,photo)
        elif update["result"][-1]["message"].get("voice",False):
            chat_id=update["result"][-1]["message"]["chat"]["id"]
            voice=update["result"][-1]["message"]["voice"]["file_id"]
            send_voice(chat_id,voice)
        elif update["result"][-1]["message"].get("document",False):
            chat_id=update["result"][-1]["message"]["chat"]["id"]
            document=update["result"][-1]["message"]["document"]["file_id"]
            send_document(chat_id,document)
        elif update["result"][-1]["message"].get("video",False):
            chat_id=update["result"][-1]["message"]["chat"]["id"]
            video=update["result"][-1]["message"]["video"]["file_id"]
            send_video(chat_id,video)
        elif update["result"][-1]["message"].get("dice",False):
            chat_id=update["result"][-1]["message"]["chat"]["id"]
            emoji=update["result"][-1]["message"]["dice"]["emoji"]
            send_dice(chat_id,emoji)
        elif update["result"][-1]["message"].get("contact",False):
            chat_id=update["result"][-1]["message"]["chat"]["id"]
            number=update["result"][-1]["message"]["contact"]["phone_number"]
            fname=update["result"][-1]["message"]["contact"]["first_name"]
            send_contact(chat_id,number,fname)
        else:
            print(-1)

    sleep(0.5)