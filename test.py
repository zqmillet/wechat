import urwid
import wxpy

text1 = urwid.Text('2345')
text2 = urwid.Text('23333', align = 'right')

filler1 = urwid.Filler(text1)
filler2 = urwid.Filler(text2)

class ChatListItem(urwid.Filler):
    name = None
    text = None

    def __init__(self, name, text):
        self.name = urwid.Text(name)
        self.text = urwid.Text(text, align = 'right')

class ChatListBox(urwid.ListBox):
    def __init__(self, chat_list_item_list):
        widget_list = list()
        for chat_list_item in chat_list_item_list:
            widget_list.append(chat_list_item.name)
            widget_list.append(chat_list_item.text)
            widget_list.append(urwid.Divider('─'))
        widget_list.pop()
        super(ChatListBox, self).__init__(urwid.SimpleListWalker(widget_list))

bot = wxpy.Bot(cache_path=True, console_qr=True)
import pdb; pdb.set_trace()
chat_list_item_list = list()
for chat in bot.chats():
    chat_list_item_list.append(ChatListItem(chat.raw['RemarkName'], chat.raw['NickName']))
listbox = ChatListBox(chat_list_item_list)
urwid.MainLoop(listbox).run()
