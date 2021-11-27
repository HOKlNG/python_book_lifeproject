import json
import requests
import datetime
import os
from common.config import Config

#토큰 저장 파일 명
KAKAO_TOKEN_FILE = 'kakao_token.json'

def save_tokens(filename,tokens):
    with open(filename, 'w') as f:
        json.dump(tokens,f)

def load_token(filename):
    with open(filename) as f:
        tokens = json.load(f)

    return tokens

def update_token(app_key, filename):
    tokens = load_token(filename)

    url = "https://kauth.kako.com/oauth/token"

    data={
        "grant_type": "refresh_token",
        "client_id": Config.get('DEV_KAKAO_DEVELOP'), #app key
        "refresh_token": tokens['refresh']
    }
    res = requests.post(url, data=data)

    if res.status_code != 200:
        print(res.status_code)
        print(res.reason)

    else:
        print(res.json())

        #기존파일백업
        now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_filename = filename+"."+now

        os.rename(filename,backup_filename)

        #갱신토큰저장
        tokens['access_token'] = res.json()['accesstoken']
        save_tokens(filename, tokens)

    return tokens

if __name__ == "__main__":
    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": Config.get('DEV_KAKAO_DEVELOP'), #app key
        "redirect_uri": "https://localhost.com",
        "code": Config.get('DEV_KAKAO_MSG_CODE')
    }

    res = requests.post(url,data=data)
    if res.status_code != 200:
        print(res.status_code)
        print(res.reason)
    else:
        tokens = res.json()
        save_tokens(KAKAO_TOKEN_FILE, tokens)