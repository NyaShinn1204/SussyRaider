import random
from httpx import Client
from httpx_socks import SyncProxyTransport
import utilities.header as header
import requests
import string
import random
import main as main
import threading
import asyncio

def randomstring(n):
    randlst = [random.choice(string.ascii_letters + string.digits)
               for i in range(n)]
    return ''.join(randlst)

def check(sussyraider, mode, proxysetting, proxies, proxytype, tokens):
    threading.Thread(target=check_thread, args=(sussyraider, mode, proxysetting, proxies, proxytype, tokens)).start()
    
def check_thread(sussyraider, mode, proxysetting, proxies, proxytype, tokens):
    try:
        lines = []
        if mode == False:
            loop = asyncio.new_event_loop()
            async def run(loop):
                async def run_req(token):
                    return await loop.run_in_executor(None, token_check, sussyraider, proxysetting, proxies, proxytype, token)
                for token in tokens:
                    lines.append(token)
                tasks = [run_req(token) for token in lines]
                return await asyncio.gather(*tasks)
            loop.run_until_complete(run(loop))
        if mode == True:
            for token in tokens:
                threading.Thread(target=token_check, args=(sussyraider, proxysetting, proxies, proxytype, token)).start()
    except Exception as err: print("[err] tokenchecker:check_thread:"+str(err))

def token_check(sussyraider, proxysetting, proxies, proxytype, token):
    request = requests.Session()
    req_header = header.request_header(token)
    headers = req_header[0]
    while True:
        try:
            request = Client()
            if proxysetting == True:
                proxy = random.choice(proxies)
                request = Client(transport=SyncProxyTransport.from_url(f'{proxytype}://{proxy}'))
            x = request.post(f"https://discord.com/api/v9/invites/"+randomstring(8), headers=headers)
        except:
            break
        finally:
            request.close()
        if x.status_code == 400:
            sussyraider.update_token(True, token)
        else:
            sussyraider.update_token(False, token)
        break