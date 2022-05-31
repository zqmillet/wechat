from utilities.wechat_bot import WechatBot
from itchat import Core

core = Core()
core.auto_login(enableCmdQR=2, statusStorageDir='wxpy.pkl', hotReload=True)
import pdb; pdb.set_trace()
# bot = WechatBot(console_qr=True, cache_path=True)
# bot.enable_puid()
# chats = bot.chats()

# import pdb; pdb.set_trace()
# message, *_ = bot.messages
