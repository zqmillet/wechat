import urwid

from dictionary import Dictionary

class ChatListBox(urwid.Filler):
    pass

text = urwid.Text('12345')
filler = urwid.Filler(text, height = 1)
linebox = urwid.LineBox(filler, title = '1234', title_align = 'left')

urwid.MainLoop(linebox).run()

