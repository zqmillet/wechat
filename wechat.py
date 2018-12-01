import urwid

from dictionary import Dictionary

class ChatListBox(urwid.Filler):
    pass

text = urwid.Text('12345')
filler = urwid.Filler(text)
linebox = urwid.LineBox(filler)

urwid.MainLoop(linebox).run()

