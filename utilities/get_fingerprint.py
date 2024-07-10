import requests

def get_fingerprint():
    session = requests.Session()
    response = session.get("https://discord.com/api/v9/experiments")
    if response.status_code == 200:
        data = response.json()
        fingerprint = data["fingerprint"]
        return fingerprint
    else:
        return
