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


    template ={
        "object_type": "list",
        "header_title": "초밥사진",
        "header_link": {
            "web_url": "www.naver.com",
            "mobile_web_url": "www.naver.com"
        },
        "contents": [
            {
                "title": "1.광어초밥",
                "description": "광어는맛있다.",
                "image_url": "https://search1.kakaocdn.net/argon/0x200_85_hr/8x5qcdbcQwi",
                "image_width": 50, "image_height": 5,
                "link":{
                    "web_url": "www.naver.com",
                    "mobile_web_url": "www.naver.com"
                }
            },
            {
                "title": "2.참치초밥",
                "description": "참치는맛있다.",
                "image_url": "https://search2.kakaocdn.net/argon/0x200_85_hr/IJIToH1S7J1",
                "image_width": 50, "image_height": 5,
                "link": {
                    "web_url": "www.naver.com",
                    "mobile_web_url": "www.naver.com"
                }
            }
        ],
        "button": [
            {
                "title": "웹으로이동",
                "link":{
                    "web_url": "www.naver.com",
                    "mobile_web_url": "www.naver.com"
                }
            }
        ]
    }


    data={
        "template_object": json.dumps(template)
    }

    res = requests.post(url, headers=headers, data=data)

    if res.status_code != 200:
        print(res.reason)
    else:
        print('메시지를 성공적으로 보냈습니다.')