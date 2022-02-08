import logging

import requests
from environs import Env


def get_work_status(url, token):
    headers = {
        'Authorization': f'Token {token}'
    }
    params = {
        'timestamp': 1555493856
    }
    while True:
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            logging.info(response.json())
        except requests.exceptions.ReadTimeout as error:
            logging.critical(error)


def main():
    env = Env()
    env.read_env()

    work_status_link = 'https://dvmn.org/api/long_polling/'
    devman_token = env.str('TOKEN')

    get_work_status(work_status_link, devman_token)


if __name__ == "__main__":
    logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s; %(levelname)s; %(name)s; %(message)s',
            filename='logs.lod',
            filemode='w',
        )
    main()
