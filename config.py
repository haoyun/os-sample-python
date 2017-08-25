import os

# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot(console_qr=True, cache_path=True)

# 给机器人自己发送消息
bot.self.send('H给机器人自己发送消息')
# 给文件传输助手发送消息
bot.file_helper.send('给文件传输助手发送消息')

# 回复发送给自己的消息，可以使用这个方法来进行测试机器人而不影响到他人
@bot.register(bot.self, except_self=False)
def reply_self(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
