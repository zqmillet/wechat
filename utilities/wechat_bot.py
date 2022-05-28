import wxpy
import html
import itchat.utils

itchat.utils.htmlParser.unescape = html.unescape
WechatBot = wxpy.Bot
