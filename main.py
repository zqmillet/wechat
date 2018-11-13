import urwid

def show_or_exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    text.set_text(text.get_text()[0] + key)
    if key == 'r':
        text.set_align_mode('right')

pelette = {
    ('banner', 'black', 'light gray'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue')
}

text = urwid.Text(('banner', 'Hello World'), align = 'center')
map1 = urwid.AttrMap(text, 'streak')
fill = urwid.Filler(map1)
map2 = urwid.AttrMap(fill, 'bg')
loop = urwid.MainLoop(map2, pelette, unhandled_input = show_or_exit)
loop.run()
