import os
import requests
from dotenv import load_dotenv

load_dotenv() # .env파일의 변수를 운영체제의 환경변수에 저장 (업로드)

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN') # 파일에서 사용할 수 있도록 가져오기

URL = f'https://api.telegram.org/bot{TOKEN}'

method = 'getUpdates'

res = requests.get(f'{URL}/{method}')

res_dict = res.json()

user_input = res_dict['result'][-1]['message']['text']
user_id = res_dict['result'][-1]['message']['from']['id']

print(user_id, user_input)

SEND_MSG_URL = f'{URL}/sendMessage?chat_id={user_id}&text={user_input}' # ? 뒤는 파라미터 & 파라미터 이을 때

requests.get(SEND_MSG_URL)