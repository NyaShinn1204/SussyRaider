import re
import requests

def get_buildnum():
    session = requests.Session()
    text = session.get("https://discord.com/login").text 
    script_url = 'https://discord.com/assets/' + re.compile(r'\d+\.\w+\.js|sentry\.\w+\.js').findall(text)[-1]
    text = session.get(script_url).text
    index = text.find("buildNumber") + 26
    build_num = int(text[index:index + 6])
    return build_num