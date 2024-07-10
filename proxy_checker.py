import threading
import requests

def check(sussyraider, proxies, types):
    threading.Thread(target=check_thread, args=(sussyraider, proxies, types)).start()
    
def check_thread(sussyraider, proxies, types):
    lines = []
    for proxy in proxies:
        threading.Thread(target=check_proxy, args=(sussyraider, proxy, types, )).start()
    
def check_proxy(sussyraider, proxy, types):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    try:
        req = requests.get('https://www.google.com/', headers=headers, proxies={'https': f'{types}://{proxy}', 'http': f'{types}://{proxy}'}, timeout=10)
        if req.ok:
            sussyraider.update_proxy(True, proxy)
            return
    except: 
        pass
    sussyraider.update_proxy(False, proxy)