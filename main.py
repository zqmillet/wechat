import readline
from rich import print
from rich.layout import Layout
from rich.layout import Panel
from time import sleep

layout = Layout()
upper_panel = Panel('hello')
lower_panel = Panel('world')

layout.split_column(
    Layout(upper_panel, name='upper'),
    Layout(lower_panel, name='lower'),
)

print(layout)

# from wxpy import Bot

# bot = Bot(cache_path=True, console_qr=True)

# for friend in bot.friends():
#     if friend.name == 'Qiqi':
#         break

# @bot.register(friend)
# def print_others(msg):
#     print(msg)

# while True:
#     try:
#         message = input('>>> ')
#         friend.send_msg(message)
#     except Exception as e:
#         print(e)
