import urwid

widget1 = urwid.Edit('what is your name?\n')
widget1 = urwid.LineBox(widget1)
widget1 = urwid.Padding(widget1)
widget1 = urwid.Filler(widget1)

widget2 = urwid.Edit('what is your name?\n')
widget2 = urwid.LineBox(widget2)
widget2 = urwid.Padding(widget2)
widget2 = urwid.Filler(widget2)

vline = urwid.AttrWrap( urwid.SolidFill(u'\u2502'), 'line')

piles = urwid.Pile([('fixed', 4, widget1)] * 10)
urwid.MainLoop(urwid.Columns([('weight', 1, piles), ('fixed', 1, vline), ('weight', 2, widget2)])).run()
