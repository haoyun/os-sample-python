import os

# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot(console_qr=True, cache_path=True)
bot.self.add()
bot.self.accept()

# 给机器人自己发送消息
bot.self.send('H给机器人自己发送消息')
# 给文件传输助手发送消息
bot.file_helper.send('给文件传输助手发送消息')

# 回复发送给自己的消息，可以使用这个方法来进行测试机器人而不影响到他人
@bot.register(bot.self, except_self=False)
def reply_self(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)

# 启用 puid 属性，并指定 puid 所需的映射数据保存/载入路径
bot.enable_puid('wxpy_puid.pkl')

@bot.register()
def print_messages(msg):
    print(msg)

# 注册好友请求类消息
@bot.register(msg_types=FRIENDS)
# 自动接受验证信息中包含 'wxpy' 的好友请求
def auto_accept_friends(msg):
    # 判断好友请求中的验证文本
    if 'wxpy' in msg.text.lower():
        # 接受好友 (msg.card 为该请求的用户对象)
        new_friend = bot.accept_friend(msg.card)
        # 或 new_friend = msg.card.accept()
        # 向新的好友发送消息
        new_friend.send('哈哈，我自动接受了你的好友请求')

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
