from common.config import Config
import requests
import json

def save_image(img_url:str, filename:str):
    img_res = requests.get(img_url)

    if img_res.status_code == 200:
        with open('img_folder/'+filename, "wb") as f:
            f.write(img_res.content)
    else:
        print(img_res.status_code)
        print(img_res.reason)


if __name__ == "__main__":
    # kakao api key
    api_key_kakao = Config.get('DEV_KAKAO_DEVELOP')
    keyword = input('저장할 이미지의 검색어를 입력하세요 :')

    url = "https://dapi.kakao.com/v2/search/image"
    headers = {
        "Authorization" : f"KakaoAK {api_key_kakao}"
    }
    data = {
        "query":keyword
    }

    res = requests.post(url, headers=headers, data=data)

    if res.status_code != 200:
        #실패
        print(res.reason)

    else:
        #성공
        count = 0
        for image_info in res.json()['documents']:
            img_url=image_info["image_url"]
            print(f"[{count}th] image_url = ", img_url)
            count+=1

            file_name = f"{keyword}%d.jpg" %(count)
            save_image(img_url, file_name)