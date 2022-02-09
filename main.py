import logging

import requests
from environs import Env


def get_work_status(url, token, timestamp):
    headers = {'Authorization': f'Token {token}'}
    params = {'timestamp': timestamp}
    print(timestamp)
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    dvmn_response = response.json()
    logging.info(dvmn_response)
    return dvmn_response


def main():
    env = Env()
    env.read_env()

    work_status_link = 'https://dvmn.org/api/long_polling/'
    devman_token = env.str('TOKEN')
    timestamp = None

    while True:
        try:
            dvmn_response = get_work_status(
                work_status_link, devman_token, timestamp)
            if dvmn_response['status'] == 'timeout':
                timestamp = dvmn_response['timestamp_to_request']

        except requests.exceptions.ReadTimeout as error:
            logging.error(f' Ошибка таймаута - {error}')

        except requests.exceptions.ConnectionError as error:
            logging.error(f' Ошибка соединения - {error}')


if __name__ == "__main__":
    logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s; %(levelname)s; %(name)s; %(message)s',
            filename='logs.lod',
            filemode='w',
        )
    main()
