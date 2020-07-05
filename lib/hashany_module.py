# Thanks for https://hashtoolkit.com/decrypt-hash/
import requests
from typing import Union
from bs4 import BeautifulSoup

base_url = 'https://hashtoolkit.com/decrypt-hash/'

def crack_hash(user_hash) -> Union[list, bool]:
    """
    The function searches for the hash in the site's database.
    If it finds the hash the function returns the type of hash and the original text
    :return: False if status code != 200 or hash not found else return a list of the plain text and the hash type
    """
    resp = requests.get(base_url, params={'hash': user_hash}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'})
    soup = BeautifulSoup(resp.content, 'html.parser')
    if resp.status_code == 200:
        if not (plain := soup.find('tbody').find('td', class_='res-text').text.strip()) == user_hash.strip() and (hash_type := soup.find('tbody').find('td').text):
            return [plain, hash_type]
    return False
