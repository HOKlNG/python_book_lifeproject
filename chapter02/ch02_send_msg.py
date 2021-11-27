import json
import requests
from common.kakao_token import update_token, save_tokens, load_token
from common.config import Config
import os

if __name__ == '__main__':

    tokens = load_token('../common/kakao_token.json')

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    headers = {
        "Authorization": "Bearer "+ tokens['access_token']
    }

    data = {
        "template_object": json.dumps({"object_type": "text",
                                       "text": "Hello, world!",
                                       "link": {"web_url": "www.naver.com"}
                                       })
    }

    res = requests.post(url, headers=headers, data=data)

    if res.status_code != 200:
        print(res.reason)
    else:
        print('메시지를 성공적으로 보냈습니다.')

