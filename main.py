from urwid import WidgetDecoration, Text, MainLoop, Filler, Edit, Button, connect_signal, CheckBox, LineBox, SolidFill, ListBox, SimpleFocusListWalker

text = Text('hello ' * 1000, align='center', wrap='space')
widge = WidgetDecoration(text)
edit = Edit(caption='>>> ', multiline=True, mask='*')
button = Button('press me')
checkbox_1 = CheckBox('xxxx')

def on_click():
    print('clicked')

connect_signal(button, 'click', on_click, None)

list_box = ListBox(SimpleFocusListWalker([widge, edit, button, checkbox_1]))

# MainLoop(Filler(LineBox(checkbox_1, title='2333', title_align='left'))).run()
MainLoop(list_box).run()
