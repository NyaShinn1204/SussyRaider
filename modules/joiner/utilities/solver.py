import re
import time
import httpx

from colorama import Fore

import modules.joiner.utilities.solver as get_balance

def extract(format_token):
    if re.compile(r"(.+):").match(format_token):
        return format_token.split(":")[1]
    else:
        token = format_token
    return token

def extractfi(input_str):
  if len(input_str) >= 5:
    replaced_str = input_str[:-5] + '*' * 5
    return replaced_str
  else:
    return input_str

def captcha_bypass_capsolver(token, siteurl, sitekey, api):
    if get_balance.get_balance_capsolver == 0.0:
        return
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    startedSolving = time.time()
    json = {
        "clientKey": api,
        "task": {
            "type": "HCaptchaTaskProxyLess",
            "websiteURL": siteurl,
            "websiteKey": sitekey,
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = httpx.post('https://api.capsolver.com/createTask', headers=headers, json=json)
    try:
        taskid = response.json()['taskId']
    except:
        print(f"[{Fore.LIGHTRED_EX}Error{Fore.RESET}] [solver.py] {(response.json()['errorDescription'])}")
        return 
    json = {"clientKey": api, "taskId": taskid}
    while True:
        time.sleep(1.5)
        response = httpx.post('https://api.capsolver.com/getTaskResult', headers=headers, json=json)
        if response.json()['status'] == 'ready':
            captchakey = response.json()['solution']['gRecaptchaResponse']
            print(f"[{Fore.LIGHTGREEN_EX}Info{Fore.RESET}] [solver.py] {Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX}Solved{Fore.RESET} | {Fore.YELLOW}{response[-32:]} {Fore.RESET}In {Fore.YELLOW}{round(time.time()-startedSolving)}s{Fore.RESET} | " + extract_token)
            return captchakey
        else:
            continue

def captcha_bypass_capmonster(token, siteurl, sitekey, api):
    if get_balance.get_balance_capmonster == 0.0:
        return
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    startedSolving = time.time()
    url = "https://api.capmonster.cloud/createTask"
    data = {
        "clientKey": api,
        "task":
        {
            "type": "HCaptchaTaskProxyless",
            "websiteURL": siteurl,
            "websiteKey": sitekey
        }
    }
    response = httpx.post(url,json=data)
    if response.json()['errorId'] == 0:
        task_id = response.json()['taskId']
        url = "https://api.capmonster.cloud/getTaskResult"
        data = {
            "clientKey": api,
            "taskId": task_id
        }
        response = httpx.post(url,json=data)
        while response.json()['status'] == 'processing':
            time.sleep(3)
            response = httpx.post(url,json=data)
        print(f"[{Fore.LIGHTGREEN_EX}Info{Fore.RESET}] [solver.py] {Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX}Solved{Fore.RESET} | {Fore.YELLOW}{response[-32:]} {Fore.RESET}In {Fore.YELLOW}{round(time.time()-startedSolving)}s{Fore.RESET} | " + extract_token)
        return response.json()['solution']['gRecaptchaResponse']
    else:
        print(f"[{Fore.LIGHTRED_EX}Error{Fore.RESET}] [solver.py] {(response.json()['errorDescription'])}")
        return False
    
def captcha_bypass_2cap(token, siteurl, sitekey, api):
    if get_balance.get_balance_2cap == 0.0:
        return
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    startedSolving = time.time()
    url = "https://2captcha.com/in.php?key={}&method=hcaptcha&sitekey={}&pageurl={}".format(api,sitekey,siteurl)
    response = httpx.get(url)
    if response.text[0:2] == 'OK':
        captcha_id = response.text[3:]
        url = "http://2captcha.com/res.php?key={}&action=get&id={}".format(api,captcha_id)
        response = httpx.get(url)
        while 'CAPCHA_NOT_READY' in response.text:
            time.sleep(5)
            response = httpx.get(url)
            print(response.text)
        print(response.text)
        print(f"[{Fore.LIGHTGREEN_EX}Info{Fore.RESET}] [solver.py] {Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX}Solved{Fore.RESET} | {Fore.YELLOW}{response[-32:]} {Fore.RESET}In {Fore.YELLOW}{round(time.time()-startedSolving)}s{Fore.RESET} | " + extract_token)
        return response.text.replace('OK|','') , str(time.time() - startedSolving)
    else:
        print(f"[{Fore.LIGHTRED_EX}Error{Fore.RESET}] [solver.py] {(response.text)}")
        return False

def captcha_bypass_anticaptcha(token, siteurl, sitekey, api):
    if get_balance.get_balance_anticaptcha == 0.0:
        return
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    startedSolving = time.time()
    url = "https://api.anti-captcha.com/createTask'"
    data = {
        "clientKey": api,
        "task":
        {
            "type": "HCaptchaTaskProxyless",
            "websiteURL": siteurl,
            "websiteKey": sitekey
        }
    }
    response = httpx.post(url,json=data)
    if response.json()['errorId'] == 0:
        task_id = response.json()['taskId']
        url = "https://api.anti-captcha.com/getTaskResult"
        data = {
            "clientKey": api,
            "taskId": task_id
        }
        response = httpx.post(url,json=data)
        while response.json()['status'] == 'processing':
            time.sleep(3)
            response = httpx.post(url,json=data)
        print(f"[{Fore.LIGHTGREEN_EX}Info{Fore.RESET}] [solver.py] {Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX}Solved{Fore.RESET} | {Fore.YELLOW}{response[-32:]} {Fore.RESET}In {Fore.YELLOW}{round(time.time()-startedSolving)}s{Fore.RESET} | " + extract_token)
        return response.json()['solution']['gRecaptchaResponse']
    else:
        print(f"[{Fore.LIGHTRED_EX}Error{Fore.RESET}] [solver.py] {(response.json()['errorDescription'])}")
        return False

def bypass_captcha(type, token, url, key, api):
    try:
        if type == 1:
            captcha_bypass_capsolver(token, url, key, api)
        if type == 2:
            captcha_bypass_capmonster(token, url, key, api)
        if type == 3:
            captcha_bypass_2cap(token, url, key, api)
        if type == 4:
            captcha_bypass_anticaptcha(token, url, key, api)
    except Exception as error:
        print(error)