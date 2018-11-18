import urwid

widget1 = urwid.Edit('what is your name?\n')
widget1 = urwid.LineBox(widget1)
widget1 = urwid.Padding(widget1, align = 'left', width = ('relative', 100))
widget1 = urwid.Filler(widget1, height = ('relative', 10), valign = 'top')

widget2 = urwid.Edit('what is your name?\n')
widget2 = urwid.LineBox(widget2)
widget2 = urwid.Padding(widget2, align = 'left', width = 'pack')
widget2 = urwid.Filler(widget2, height = ('relative', 10), valign = 'top')


urwid.MainLoop(urwid.Columns([urwid.Pile([widget1, widget2]), widget1, widget2])).run()
