import time
import threading
import requests
import base64
import re
import os
from colorama import Fore

import utilities.header as header
import utilities.solver as solver

pretty = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
gray = Fore.LIGHTBLACK_EX + Fore.WHITE

changenick = False ## DO NOT CHANGE

nickname = "みけねこ的うるはるしあ"

def get_filename():
  return os.path.basename(__file__)    

def printl(num, data):
  if num == "error":
    print(f"[{Fore.LIGHTRED_EX}Error{Fore.RESET}] [{get_filename()}] " + data)
  if num == "info":
    print(f"[{Fore.LIGHTGREEN_EX}Info{Fore.RESET}] [{get_filename()}] " + data)
    
def start(tokens, serverid, invitelink, memberscreen, delay, module_status, answers, apis, bypasscaptcha, delete_joinms, join_channelid):
    for token in tokens:
        threading.Thread(target=joiner_thread, args=(token, serverid, invitelink, memberscreen, module_status, answers, apis, bypasscaptcha, delete_joinms, join_channelid)).start()
        time.sleep(float(delay))

def extract(format_token):
    if re.compile(r"(.+):").match(format_token):
        return format_token.split(":")[1]
    else:
        token = format_token
    return token

def accept_rules_bypass(token, requests, serverid, invitelink):
    printl("error", "Fuck!! Fucking Discord!! Using this will lock the account!")
    return
            
def change_nicker(token, serverid, nickname):
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    req_header = header.request_header(token)
    headers = req_header
    req = requests.patch(f"https://discord.com/api/v9/guilds/{serverid}/members/@me/nick", headers=headers, json={"nick": nickname})
    if req.status_code == 200:
        print(f'Successfully Changed Nickname {gray}| ' + Fore.CYAN + extract_token + Fore.RESET)
    if req.status_code != 200:
        print(f'Error Changing Nickname {gray}| ' + Fore.CYAN + extract_token + Fore.RESET)

def delete_join_msg(token, join_channel_id):
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    req_header = header.request_header(token)
    headers = req_header
    messages = requests.get(f"https://discord.com/api/v9/channels/{join_channel_id}/messages?limit=100",headers=headers).json()
    for message in messages:
        bot_token_id = base64.b64decode(token.split(".")[0]+"==").decode()
        if message["content"] == "" and bot_token_id == message["author"]["id"]:
            deleted_join = requests.delete(f"https://discord.com/api/v9/channels/{join_channel_id}/messages/{message['id']}",headers=headers)
            if deleted_join.status_code == 204:
                printl("info", f"{pretty}Success Delete Join Message {gray}| " + Fore.CYAN + extract_token + Fore.RESET)
            else:
                printl("error", f"{pretty}Failed Delete Join Message {gray}| " + Fore.CYAN + extract_token + Fore.RESET)
                print(deleted_join.text)
            break
        
def joiner_thread(token, serverid, invitelink, memberscreen, module_status, answers, apis, bypasscaptcha, delete_joinms, join_channelid):
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    session = header.get_session.get_session()
    req_header = header.request_header_fingerprint(token)
    headers = req_header
    try:
        joinreq = session.post(f"https://discord.com/api/v9/invites/{invitelink}?inputValue=https://discord.gg/yBGsQY8A&with_counts=true&with_expiration=true", headers=headers, json={})
        if joinreq.status_code == 400:
            if bypasscaptcha == True:
                printl("info", f"{pretty}Solving Captcha{gray} | " + Fore.GREEN + extract_token + Fore.RESET)
                payload = {
                    "captcha_key": solver.bypass_captcha(answers, token, "https://discord.com", joinreq.json()['captcha_sitekey'], apis)
                }
            else:
                payload = {
                    "captcha_key": None
                }
            newresponse = session.post(f"https://discord.com/api/v9/invites/{invitelink}?inputValue=https://discord.gg/yBGsQY8A&with_counts=true&with_expiration=true", headers=headers, json=payload)
            if newresponse.status_code == 200:
                if "captcha_key" not in newresponse.json():
                    if "You need to verify your account in order to perform this action." in newresponse.json():
                        printl("error", f"{pretty}認証が必要です {gray}| " + Fore.CYAN + extract_token + Fore.RESET)
                        module_status(1, 1, 2)
                    printl("info", f"{pretty}Successfully Token Join {gray}| " + Fore.CYAN + extract_token + Fore.RESET)
                    if delete_joinms == True:
                        printl("info", f"{pretty}Deleting Join Message {gray}| " + Fore.CYAN + extract_token + Fore.RESET)
                        delete_join_msg(token, join_channelid)
                    module_status(1, 1, 1)
                if memberscreen == True:
                    accept_rules_bypass(token, joinreq.json(), serverid, invitelink)
                if changenick == True:
                    change_nicker(token, serverid, nickname)
            else:
                if "captcha_key" in joinreq.json():
                    printl("error", f"{pretty}Failed Token Join (Captcha Wrong) {gray}| " + Fore.CYAN + extract_token + Fore.RESET)
                    print(joinreq.json())
                    module_status(1, 1, 2)
                else:
                    printl("error", f"{pretty}Failed Captcha Bypass {gray}| " + Fore.CYAN + extract_token + Fore.RESET+ " | " + newresponse.text.replace("\n", ""))
        if joinreq.status_code == 200:
            if "captcha_key" not in joinreq.json():
                if "You need to verify your account in order to perform this action." in joinreq.json():
                    printl("error", f"{pretty}認証が必要です {gray}| " + Fore.CYAN + extract_token + Fore.RESET)
                    module_status(1, 1, 2)
                printl("info", f"{pretty}Successfully Token Join {gray}| " + Fore.CYAN + extract_token + Fore.RESET)
                if delete_joinms == True:
                    printl("info", f"{pretty}Deleting Join Message {gray}| " + Fore.CYAN + extract_token + Fore.RESET)
                    delete_join_msg(token, join_channelid)
                module_status(1, 1, 1)
            if memberscreen == True:
                accept_rules_bypass(token, joinreq.json(), serverid, invitelink)
            if changenick == True:
                change_nicker(token, serverid, nickname)
        if joinreq.status_code == 403:
            if joinreq.json()["message"] or "\u3053\u306e\u30e6\u30fc\u30b6\u30fc\u306f\u3001\u3053\u306e\u30b5\u30fc\u30d0\u30fc\u304b\u3089BAN\u3055\u308c\u3066\u3044\u307e\u3059\u3002" or "The user is banned from this guild." in joinreq.json():
                printl("error", f"{pretty}Banned fom Server {gray}| " + Fore.CYAN + extract_token + Fore.RESET)
                module_status(1, 1, 2)
    except Exception as err:
        print(f"[-] ERROR: {err} ")
        return