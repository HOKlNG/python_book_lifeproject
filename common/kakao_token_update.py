from common.kakao_token import update_token, save_tokens
from common.config import Config

if __name__ == "__main__":
    KAKAO_TOKEN_FILE = 'kakao_token.json'
    tokens = update_token(Config.get('DEV_KAKAO_DEVELOP'),KAKAO_TOKEN_FILE)
    save_tokens(KAKAO_TOKEN_FILE, tokens)