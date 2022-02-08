import requests
from environs import Env


def get_work_status(url, token):
    headers = {
        'Authorization': f'Token {token}'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def main():
    env = Env()
    env.read_env()

    work_status_link = 'https://dvmn.org/api/user_reviews/'
    devman_token = env.str('TOKEN')

    print(get_work_status(work_status_link, devman_token))


main()
