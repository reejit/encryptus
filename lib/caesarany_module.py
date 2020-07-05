# Thanks for https://www.dcode.fr
import requests
from string import ascii_uppercase

def encode_caesar(plain, base):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    data = {
        'tool': 'caesar-cipher',
        'plaintext': plain.replace(' ', '+'),
        'shift': base,
        'alphabet': ascii_uppercase }
    resp = requests.post('https://www.dcode.fr/api/', data=data, headers=headers)
    if resp.status_code == 200:
         return resp.json()['results']
    return False

def decode_caesar(cipher, base):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    data = {
        'tool': 'caesar-cipher',
        'ciphertext': cipher.replace(' ', '+'),
        'method': 'normal',
        'shift': base
    }
    resp = requests.post('https://www.dcode.fr/api/', data=data, headers=headers)
    if resp.status_code == 200:
        return resp.json()['results']
    return False
