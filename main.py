import urwid

txt = urwid.Text('hello world')
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill)

def show_or_exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    string, _ = txt.get_text()
    txt.set_text(string + key)

txt = urwid.Text('hello world')
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()
