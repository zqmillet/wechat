import urwid
palette = [('header', 'white', 'black'),
            ('reveal focus', 'black', 'dark cyan', 'standout'),]
items = map(lambda x: urwid.Text(x), range(500))
items = map(lambda x: urwid.AttrMap(x, None, 'reveal focus'), items)
walker = urwid.SimpleListWalker(items)
listbox = urwid.ListBox(walker)
loop = urwid.MainLoop(listbox, palette)
loop.run()
