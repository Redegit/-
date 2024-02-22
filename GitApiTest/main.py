import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.github.com"
TOKEN = os.getenv("TOKEN")
headers = {"Authorization": TOKEN} if TOKEN else {}


def get_user_info(username):
    response = requests.get(f"{BASE_URL}/users/{username}", headers=headers)
    return response


def get_user_repo_list(username):
    response = requests.get(f"{BASE_URL}/users/{username}/repos", headers=headers)
    return response


def get_user_followers(username):
    response = requests.get(f"{BASE_URL}/users/{username}/followers", headers=headers)
    return response


if __name__ == '__main__':
    print(get_user_info("Strawlll").json())
    print(get_user_repo_list("Strawlll").json())
    print(get_user_followers("Strawlll").json())
