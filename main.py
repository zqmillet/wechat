def main():
    palette = [
        ('body','black','dark cyan', 'standout'),
        ('foot','light gray', 'black'),
        ('key','light cyan', 'black', 'underline'),
        ('title', 'white', 'black',),
        ]

    footer_text = [
        ('title', "Fibonacci Set Viewer"), "    ",
        ('key', "UP"), ", ", ('key', "DOWN"), ", ",
        ('key', "PAGE UP"), " and ", ('key', "PAGE DOWN"),
        " move view  ",
        ('key', "Q"), " exits",
        ]

    def exit_on_q(input):
        if input in ('q', 'Q'):
            raise urwid.ExitMainLoop()

    listbox = urwid.ListBox(FibonacciWalker())
    footer = urwid.AttrMap(urwid.Text(footer_text), 'foot')
    view = urwid.Frame(urwid.AttrWrap(listbox, 'body'), footer=footer)
    loop = urwid.MainLoop(view, palette, unhandled_input=exit_on_q)
    loop.run()

main()
