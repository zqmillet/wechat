import urwid

ask = urwid.Edit('what is your name?\n')
top = urwid.Filler(ask)

urwid.MainLoop(urwid.Columns([top, top])).run()
