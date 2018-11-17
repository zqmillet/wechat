import urwid

palette = [('i say', 'default, bold', 'default', 'bold'),]
ask = urwid.Edit(('i say', 'what is your name?\n'))
reply = urwid.Text('')
button = urwid.Button('exit')
div = urwid.Divider()
pile = urwid.Pile([ask, div, reply, div, button])
top = urwid.Columns([pile, div], 1)

def on_ask_change(edit, new_edit_text):
    reply.set_text(('i say', 'nice to meet you, ' + new_edit_text))

def on_exit_click(button):
    raise urwid.ExitMainLoop()

urwid.connect_signal(ask, 'change', on_ask_change)
urwid.connect_signal(button, 'click', on_exit_click)

urwid.MainLoop(top, palette).run()
