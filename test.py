import urwid

text1 = urwid.Text('2345')
text2 = urwid.Text('23333', align = 'right')

filler1 = urwid.Filler(text1)
filler2 = urwid.Filler(text2)

class ChatListItem(urwid.Filler):
    name = None
    text = None

    def __init__(self, name, text):
        self.name = name
        self.text = text
        import pdb; pdb.set_trace()
        super(ChatListItem, self).__init__(text1)

class ChatListBox(urwid.ListBox):
    def __init__(self, widget_list):
        super(ChatListBox, self).__init__(urwid.SimpleListWalker(widget_list))

listbox = ChatListBox([
    ChatListItem('123', '333'),
    text2,
    urwid.Divider('─', top = 0),
    text1,
    text2])
urwid.MainLoop(listbox).run()
