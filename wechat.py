import urwid

from dictionary import Dictionary

class ChatListBox(urwid.Filler):
    pass

text = urwid.Text('12345', align = 'right')
linebox = urwid.LineBox(text, title = '1234', title_align = 'left')
listbox = urwid.ListBox(urwid.SimpleListWalker([linebox, linebox, linebox]))

detaillinebox = urwid.LineBox(urwid.Text(''), title = 'jajaj', title_align = 'left')
detaillistbox = urwid.ListBox(urwid.SimpleListWalker([detaillinebox, detaillinebox]))

columns = urwid.Columns([(20, listbox), detaillistbox])

urwid.MainLoop(columns).run()

