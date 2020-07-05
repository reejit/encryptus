import telebot
import requests
from typing import Union
from bs4 import BeautifulSoup
from random import choice
from lib.baseany_module import encode_base, decode_base
from lib.caesarany_module import encode_caesar, decode_caesar
from lib.hashany_module import crack_hash
from lib.atbash_module import atbash

class Encryptus:
    def __init__(self):
        self.TOKEN = 'TOKEN'
        self.bot = telebot.TeleBot(token=self.TOKEN)

        self.main(self.bot)

        self.bot.polling()

    def __repr__(self):
        return f'Created by Roi Levi'

    def main(self, bot):
        @bot.message_handler(commands=['about'])
        def about(message) -> None:
            chat_id = message.chat.id
            text = u'Created by *JonSkeet*. Latest stable source code available [on Github](https://github.com/r0eilevi/Encryptus), All Rights Reserved \u2661'
            bot.send_message(chat_id=chat_id, text=text, parse_mode='Markdown', disable_web_page_preview=True)

        @bot.message_handler(commands=['version'])
        def version(message) -> None:
            chat_id = message.chat.id
            version_bot = '*Current stable version*: _1.00_'
            bot.send_message(chat_id=chat_id, text=version_bot, parse_mode='Markdown')

        @bot.message_handler(commands=['help'])
        def help_(message) -> None:
            chat_id = message.chat.id
            help_message = f"Hi, *{message.from_user.first_name}*, It's a pleasure to meet you!"
            bot.send_message(chat_id=chat_id, text=help_message, parse_mode='Markdown')
            
        @bot.message_handler(commands=['b64d', 'base64d', 'b16d', 'base16d', 'b32d', 'base32d', 'b85d', 'base85d'])
        def anybase_decode(message) -> Union[None, bool]:
            base_type = ''.join(filter(str.isdigit, ''.join(message.text.split()[0])))
            command = ''.join(message.text.split()[0])
            if not (cipher := ''.join(message.text.split(command, 1)[1])):
                bot.reply_to(message=message, text=f"*Syntax*: _(b{base_type}d|base{base_type}d <cipher>)_", parse_mode='Markdown'); return False
            if not (plain := decode_base(cipher, base_type)):
                bot.reply_to(message=message, text=f"*I'm not sure it's encoded with base{base_type}*", parse_mode='Markdown'); return False
            bot.reply_to(message=message, text=f'*{plain.decode()}*', parse_mode='Markdown')

        @bot.message_handler(commands=['b64e', 'base64e', 'b16e', 'base16e', 'b32e', 'base32e', 'b85e', 'base85e'])
        def anybase_encode(message) -> Union[None, bool]:
            base_type = ''.join(filter(str.isdigit, ''.join(message.text.split()[0])))
            command = ''.join(message.text.split()[0])
            if not (plain := ''.join(message.text.split(command, 1)[1])):
                bot.reply_to(message=message, text=f"*Syntax*: _(b{base_type}e|base{base_type}e <plain>)_", parse_mode='Markdown'); return False
            if not (cipher := encode_base(plain, base_type)):
                bot.reply_to(message=message, text='*Whoops, I caught an error!*', parse_mode='Markdown'); return False
            bot.reply_to(message=message, text=f'*{cipher.decode()}*', parse_mode='Markdown')

        @bot.message_handler(commands=[f'caesar{x}e' for x in range(27)])
        def anycaesar_encode(message) -> Union[None, bool]:
            caesar_mode = ''.join(filter(str.isdigit, ''.join(message.text.split()[0])))
            command = ''.join(message.text.split()[0])
            if not (plain := ''.join(message.text.split(command, 1)[1])):
                bot.reply_to(message=message, text=f'*Syntax*: _(caesar{caesar_mode}e <plain>)_', parse_mode='Markdown'); return False
            if not (cipher := encode_caesar(plain, caesar_mode)):
                bot.reply_to(message=message, text='*Connection Error with the API service*', parse_mode='Markdown'); return False
            bot.reply_to(message=message, text=f'*{cipher.replace("+", " ")}*', parse_mode='Markdown')

        @bot.message_handler(commands=[f'caesar{x}d' for x in range(27)])
        def anycaesar_decode(message) -> Union[None, bool]:
            caesar_mode = ''.join(filter(str.isdigit, ''.join(message.text.split()[0])))
            command = ''.join(message.text.split()[0])
            if not (cipher := ''.join(message.text.split(command, 1)[1])):
                bot.reply_to(message=message, text=f"*Syntax*: _(caesar{caesar_mode}d <cipher>)_", parse_mode='Markdown'); return False
            if not (plain := decode_caesar(cipher, caesar_mode)):
                bot.reply_to(message=message, text=f"*Connection Error with the API service*", parse_mode='Markdown'); return False
            bot.reply_to(message=message, text=f'*{plain.replace("+", " ")}*', parse_mode='Markdown')

        @bot.message_handler(commands=['catfact', 'cfact'])
        def catfact(message) -> bool:
            resp = requests.get('https://www.care.com/c/stories/6045/101-amazing-cat-facts-fun-trivia-about-your-feline-friend/')
            if not resp.status_code == 200:
                self.bot.reply_to(message=message, text='*Connection Error*', parse_mode='Markdown'); return False
            soup = BeautifulSoup(resp.content, 'html.parser')
            random_fact = choice(soup.find('div', class_='tw-mt-3 content').find_all('li')).text
            self.bot.reply_to(message, text=random_fact)
            return True

        @bot.message_handler(commands=['joke'])
        def joke(message) -> bool:
            resp = requests.get('https://bestlifeonline.com/actually-funny-bad-jokes/')
            if not resp.status_code == 200:
                self.bot.reply_to(message=message, text='*Connection Error*', parse_mode='Markdown'); return False
            soup = BeautifulSoup(resp.content, 'html.parser')
            random_joke = choice(soup.find('div', class_='content').find_all('li')).text
            self.bot.reply_to(message, text=random_joke)
            return True

        @bot.message_handler(commands=['chash', 'crackhash'])
        def anyhash_crack(message) -> Union[None, bool]:
            command = ''.join(message.text.split()[0])
            if not (hash_ := ''.join(message.text.split(command, 1)[1])):
                bot.reply_to(message=message, text=f"*Syntax*: _(chash|crackhash <hash>)_", parse_mode='Markdown'); return False
            if not (crack_hash(hash_)):
                bot.reply_to(message=message, text=f"*Hash not Found/Invalid Hash!*", parse_mode='Markdown'); return False
            plain, hash_type = crack_hash(hash_)[0], crack_hash(hash_)[1]
            bot.reply_to(message=message, text=f'{hash_type}: {plain}')

        @bot.message_handler(commands=['atbash', 'ab'])
        def atbash_func(message) -> Union[None, bool]:
            command = ''.join(message.text.split()[0])
            if not (text := ''.join(message.text.split(command, 1)[1])):
                bot.reply_to(message=message, text=f"*Syntax*: _(atbash|ab <text>)_", parse_mode='Markdown'); return False
            result = atbash(text)
            bot.reply_to(message=message, text=f'{result}')
