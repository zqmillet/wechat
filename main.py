import urwid

palette = [('i say', 'default, bold', 'default', 'bold'),]
ask1 = urwid.Edit(('i say', 'what is your name?\n'))
ask2 = urwid.Edit(('i say', 'what is your name?\n'))
top = urwid.Columns([ask1, ask2], 1)

urwid.MainLoop(top, palette).run()
