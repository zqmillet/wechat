from utilities.wechat_bot import WechatBot

bot = WechatBot(console_qr=True, cache_path=True)
bot.enable_puid()
chats = bot.chats()

import pdb; pdb.set_trace()
