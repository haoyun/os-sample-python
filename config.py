import os

# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot(console_qr=1, cache_path=True)

# 给机器人自己发送消息
bot.self.send('Hello World!')
# 给文件传输助手发送消息
bot.file_helper.send('Hello World!')

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
