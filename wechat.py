import urwid

from dictionary import Dictionary

class ChatListBox(urwid.Filler):
    pass

text = urwid.Text('12345')
filler = urwid.Filler(text)
linebox = urwid.LineBox(urwid.BoxAdapter(filler, height = 2), title = '1234', title_align = 'left')

urwid.MainLoop(linebox).run()

