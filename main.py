import urwid

def question():
    return urwid.Pile([urwid.Edit(('i say', 'what is your name?\n'))])

def answer(name):
    return urwid.Text(('i say', f'nice to meet you {name}\n'))

class ConversationListBox(urwid.ListBox):
    def __init__(self):
        body = urwid.SimpleFocusListWalker([question()])
        super().__init__(body)

    def keypress(self, size, key):
        key = super().keypress(size, key)
        if key != 'enter':
            return key

        name = self.focus[0].edit_text
        if not name:
            raise urwid.ExitMainLoop()

        self.focus.contents[1:] = [(answer(name), self.focus.options())]
        pos = self.focus_position
        self.body.insert(pos + 1, question())
        self.focus_position = pos + 1

urwid.MainLoop(ConversationListBox()).run()
