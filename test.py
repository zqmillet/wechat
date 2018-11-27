import urwid

text1 = urwid.Text('2345')
text2 = urwid.Text('23333', align = 'right')

filler1 = urwid.Filler(text1)
filler2 = urwid.Filler(text2)

class ChatListItem(object):
    name = None
    text = None

    def __init__(self, name, text):
        self.name = name
        self.text = name

class ChatListBox(urwid.ListBox):
    def __init__(self, widget_list):
        super(ChatListBox, self).__init__(urwid.SimpleListWalker(widget_list))

listbox = ChatListBox([
    text1,
    text2,
    urwid.Divider('─', top = 0),
    text1,
    text2])
urwid.MainLoop(listbox).run()
