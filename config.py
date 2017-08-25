import os

# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot(console_qr=True, cache_path=True)

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
