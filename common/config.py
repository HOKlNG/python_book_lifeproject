import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_FILE_PATH = os.path.join(BASE_DIR, 'secret.json')


class Config:
    with open(SECRET_FILE_PATH) as f:
        secret_dict = json.loads(f.read())

    @staticmethod
    def get(key: str):
        try:
            return Config.secret_dict[key]
        except KeyError:
            error_msg = "Set the '{0}' environment variable".format(key)
            raise print(error_msg)