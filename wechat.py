import urwid

from dictionary import Dictionary

class ChatListBox(urwid.Filler):
    pass

text = urwid.Text('12345', align = 'right')
linebox = urwid.LineBox(text, title = '1234', title_align = 'left')
listbox = urwid.ListBox(urwid.SimpleListWalker([linebox, linebox, linebox]))

urwid.MainLoop(listbox).run()

