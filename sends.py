from settings import*
import requests

def send_message(chat_id: int, text, parse_mode=False):
    params={
        "chat_id":chat_id,
        "text":text
    }

    if parse_mode:
        params["parse_mode"]=parse_mode
    requests.get(url+"/sendMessage",params=params)

def send_contact(chat_id: int, number,fname,parse_mode=False):
    params={
        "chat_id":chat_id,
        "phone_number":number,
        "first_name":fname
    }

    requests.get(url+"/sendContact",params=params)

def send_location(chat_id: int, text, parse_mode=False):
    pass

def send_photo(chat_id: int, photo, parse_mode=False):
    params={
        "chat_id":chat_id,
        "photo":photo
    }

    requests.get(url+"/sendPhoto",params=params)

def send_voice(chat_id: int, voice, parse_mode=False):
    params={
        "chat_id":chat_id,
        "audio":voice
    }

    requests.get(url+"/sendAudio",params=params)

def send_document(chat_id: int, document, parse_mode=False):
    params={
        "chat_id":chat_id,
        "document":document
    }

    requests.get(url+"/sendDocument",params=params)

def send_video(chat_id: int, video, parse_mode=False):
    params={
        "chat_id":chat_id,
        "video":video
    }

    requests.get(url+"/sendVideo",params=params)

def send_dice(chat_id: int, emoji, parse_mode=False):
    params={
        "chat_id":chat_id,
        "emoji":emoji
    }

    requests.get(url+"/sendDice",params=params)

# def send_message(chat_id: int, text, parse_mode=False):
#     pass