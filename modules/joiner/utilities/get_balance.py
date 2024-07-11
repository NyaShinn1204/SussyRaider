import requests

def extractfi(input_str):
  if len(input_str) >= 5:
    replaced_str = input_str[:-5] + '*' * 5
    return replaced_str
  else:
    return input_str

def get_balance_capsolver(api):
    resp = requests.post(f"https://api.capsolver.com/getBalance", json={"clientKey": api})
    if resp.status_code == 200:
        balance = resp.json()["balance"]
        if balance == 0.0:
            print(f"[+] Working Key: {extractfi(api)}  But Balance 0.0$")
        else:
            print(f"[+] Working Key: {extractfi(api)}  Balance: {balance}$")
        return resp.json()["balance"]
    elif "ERROR_KEY_DOES_NOT_EXIST" in resp.text:
        print(f"[-] Invalid Key: {extractfi(api)}")
        return 0.0
    else:
        print(f"[-] Invalid Key Or Exception Error   Key: {extractfi(api)} Status Code: {resp.status_code}")
        return 0.0

def get_balance_capmonster(api):
    resp = requests.post(f"https://api.capmonster.cloud/getBalance", json={"clientKey": api})
    if resp.status_code == 200:
        balance = resp.json()["balance"]
        if balance == 0.0:
            print(f"[+] Working Key: {extractfi(api)}  But Balance 0.0$")
        else:
            print(f"[+] Working Key: {extractfi(api)}  Balance: {balance}$")
        return resp.json()["balance"]
    elif "ERROR_KEY_DOES_NOT_EXIST" in resp.text:
        print(f"[-] Invalid Key: {extractfi(api)}")
        return 0.0
    else:
        print(f"[-] Invalid Key Or Exception Error   Key: {extractfi(api)} Status Code: {resp.status_code}")
        return 0.0

def get_balance_2cap(api):
    resp = requests.post(f"https://api.2captcha.com/getBalance", json={"clientKey": api})
    if resp.status_code == 200:
        balance = resp.json()["balance"]
        if balance == 0.0:
            print(f"[+] Working Key: {extractfi(api)}  But Balance 0.0$")
        else:
            print(f"[+] Working Key: {extractfi(api)}  Balance: {balance}$")
        return resp.json()["balance"]
    elif "ERROR_KEY_DOES_NOT_EXIST" in resp.text:
        print(f"[-] Invalid Key: {extractfi(api)}")
        return 0.0
    else:
        print(f"[-] Invalid Key Or Exception Error   Key: {extractfi(api)} Status Code: {resp.status_code}")
        return 0.0
    
def get_balance_anticaptcha(api):
    resp = requests.post(f"https://api.anti-captcha.com/getBalance", json={"clientKey": api})
    if resp.status_code == 200:
        balance = resp.json()["balance"]
        if balance == 0.0:
            print(f"[+] Working Key: {extractfi(api)}  But Balance 0.0$")
        else:
            print(f"[+] Working Key: {extractfi(api)}  Balance: {balance}$")
        return resp.json()["balance"]
    elif "ERROR_KEY_DOES_NOT_EXIST" in resp.text:
        print(f"[-] Invalid Key: {extractfi(api)}")
        return 0.0
    else:
        print(f"[-] Invalid Key Or Exception Error   Key: {extractfi(api)} Status Code: {resp.status_code}")
        return 0.0