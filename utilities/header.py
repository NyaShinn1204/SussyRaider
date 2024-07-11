import base64
import json
import random

import utilities.get_cookie as get_cookie
import utilities.get_buildnum as get_buildnum
import utilities.get_fingerprint as get_fingerprint
import utilities.get_sesion as get_sesion
import utilities.random_agent as random_agent

def request_header(token):
    agent_string = random_agent.random_agent()
    buildnum = get_buildnum.get_buildnum()
    browser_data = agent_string.split(" ")[-1].split("/")
    possible_os_list = ["Windows", "Macintosh"]
    for possible_os in possible_os_list:
        if possible_os in agent_string:
            agent_os = possible_os
    if agent_os == "Macintosh":
        os_version = f'Intel Mac OS X 10_15_{str(random.randint(5, 7))}'
    else:
        os_version = "10"
    cookie_string = get_cookie.get_cookie()
    device_info = {
        "os": agent_os,
        "browser": browser_data[0],
        "device": "",
        "system_locale": "ja-JP",
        "browser_user_agent": agent_string,
        "browser_version": browser_data[1],
        "os_version": os_version,
        "referrer": "",
        "referring_domain": "",
        "referrer_current": "",
        "referring_domain_current": "",
        "release_channel": "stable",
        "client_build_number": buildnum,
        "client_event_source": None
    }
    headers = {
        "Accept":"*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US",
        "Authorization": token,
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Host": "discord.com",
        "Origin": "https://discord.com",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "sec-ch-ua-platform": "Windows",
        "sec-ch-ua-mobile": "?0",
        "TE": "Trailers",
        "User-Agent": agent_string,
        "X-Debug-Options": "bugReporterEnabled",
        "X-Discord-Locale": "ja",
        "X-Discord-Timezone": "Asia/Tokyo",
        "X-Super-Properties": base64.b64encode(json.dumps(device_info).encode('utf-8')).decode("utf-8")
    }
    headers2 = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US',
        'Cookie': cookie_string,
        'DNT': '1',
        'origin': 'https://discord.com',
        'TE': 'Trailers',
        "X-Discord-Locale": "ja",
        "X-Discord-Timezone": "Asia/Tokyo",
        'X-Super-Properties': base64.b64encode(json.dumps(device_info).encode('utf-8')).decode("utf-8"),
        'authorization': token,
        'user-agent': agent_string
    }
    return headers, headers2

def request_header_fingerprint(token):
    agent_string = random_agent.random_agent()
    fingerprint = get_fingerprint.get_fingerprint()
    buildnum = get_buildnum.get_buildnum()
    browser_data = agent_string.split(" ")[-1].split("/")
    possible_os_list = ["Windows", "Macintosh"]
    for possible_os in possible_os_list:
        if possible_os in agent_string:
            agent_os = possible_os
    if agent_os == "Macintosh":
        os_version = f'Intel Mac OS X 10_15_{str(random.randint(5, 7))}'
    else:
        os_version = "10"
    device_info = {
        "os": agent_os,
        "browser": browser_data[0],
        "device": "",
        "system_locale": "ja-JP",
        "browser_user_agent": agent_string,
        "browser_version": browser_data[1],
        "os_version": os_version,
        "referrer": "",
        "referring_domain": "",
        "referrer_current": "",
        "referring_domain_current": "",
        "release_channel": "stable",
        "client_build_number": buildnum,
        "client_event_source": None
    }
    headers = {
        "Accept":"*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US",
        "Authorization": token,
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Cookie": get_cookie.get_cookie(),
        "Host": "discord.com",
        "Origin": "https://discord.com",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "sec-ch-ua-platform": "Windows",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "TE": "Trailers",
        "User-Agent": agent_string,
        "x-fingerprint": fingerprint,
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "ja",
        "x-discord-timezone": "Asia/Tokyo",
        "x-super-properties": base64.b64encode(json.dumps(device_info).encode('utf-8')).decode("utf-8")
    }
    return headers