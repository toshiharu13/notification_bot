import logging
import textwrap

import requests
import telegram
from environs import Env
from time import sleep


def get_work_status(url, token, timestamp):
    headers = {'Authorization': f'Token {token}'}
    params = {'timestamp': timestamp}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    dvmn_response = response.json()
    logging.info(dvmn_response)
    return dvmn_response


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s; %(levelname)s; %(name)s; %(message)s',
        filename='logs.lod',
        filemode='w',
    )
    env = Env()
    env.read_env()

    work_status_link = 'https://dvmn.org/api/long_polling/'
    devman_token = env.str('DVMN_TOKEN')
    timestamp = None
    bot_token = env.str('TG_BOT_TOKEN')
    chat_id = env.str('TG_CHAT_ID')
    bot = telegram.Bot(token=bot_token)
    error_connect_count = 0
    sleep_time = 90
    errors_quantity = 5

    bot.send_message(text='Привет !', chat_id=chat_id)

    while True:
        try:
            dvmn_response = get_work_status(
                work_status_link, devman_token, timestamp)
            last_attempt = dvmn_response['new_attempts'][0]
            if dvmn_response['status'] == 'timeout':
                timestamp = dvmn_response['timestamp_to_request']
            if dvmn_response['status'] == 'found':
                lesson = last_attempt['lesson_title']
                lesson_url = last_attempt['lesson_url']
                lesson_result = (
                    'К сожалению, в работе есть ошибки'
                    if last_attempt['is_negative']
                    else 'Преподаватель принял задачу'
                )
                bot_text = textwrap.dedent(f'''\
                Преподаватель проверил работу - {lesson}
                {lesson_result}. Ссылка - 
                {lesson_url}''')
                bot.send_message(text=bot_text, chat_id=chat_id)

        except requests.exceptions.ReadTimeout as error:
            logging.error(f' Ошибка таймаута - {error}')

        except requests.exceptions.ConnectionError as error:
            logging.error(f' Ошибка соединения - {error}')
            error_connect_count += 1
            if error_connect_count > errors_quantity:
                logging.warning(
                    'Достигнут максимум попыток соединений - таймаут')
                sleep(sleep_time)
                error_connect_count = 0


if __name__ == "__main__":
    main()
