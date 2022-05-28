from urwid import WidgetWrap
from urwid import LineBox
from urwid import ListBox
from urwid import Columns
from urwid import Filler
from urwid import Frame
from urwid import Text
from urwid import AttrWrap
from urwid import AttrMap
from urwid import SimpleFocusListWalker
from urwid import ExitMainLoop
from urwid import MainLoop
from urwid import register_signal
from urwid import emit_signal
from urwid import disconnect_signal
from urwid import connect_signal
from urwid import raw_display

class ListItem(WidgetWrap):
    def __init__ (self, country):
        self.content = country
        name = country["name"]
        text = AttrWrap(LineBox(Text('gouliguojiashengsiyi'), title=name, title_align='left'), "country", "country_selected")
        super().__init__(text)

    def selectable(self):
        return True

    def keypress(self, size, key):
        return key

class ListView(WidgetWrap):
    def __init__(self):
        register_signal(self.__class__, ['show_details'])
        self.walker = SimpleFocusListWalker([])
        WidgetWrap.__init__(self, ListBox(self.walker))

    def modified(self):
        focus_w, _ = self.walker.get_focus()
        emit_signal(self, 'show_details', focus_w.content)

    def set_data(self, countries):
        countries_widgets = [ListItem(c) for c in countries]
        disconnect_signal(self.walker, 'modified', self.modified)

        while len(self.walker) > 0:
            self.walker.pop()

        self.walker.extend(countries_widgets)
        connect_signal(self.walker, "modified", self.modified)
        self.walker.set_focus(0)

class DetailView(WidgetWrap):
    def __init__ (self):
        t = Text("")
        super().__init__(t)

    def set_country(self, c):
        s = f'Name: {c["name"]}\nPop:  {c["pop"]}\nGDP:  {c["gdp"]}'
        self._w.set_text(s)

class App(object):
    def unhandled_input(self, key):
        if key in ('q',):
            raise ExitMainLoop()

    def show_details(self, country):
        self.detail_view.set_country(country)

    def __init__(self):
        self.palette = {
            ("bg",               "black",       "white"),
            ("country",          "black",       "white"),
            ("country_selected", "black",       "yellow"),
            ("footer",           "white, bold", "dark red")
        }

        self.list_view = ListView()
        self.detail_view = DetailView()

        connect_signal(self.list_view, 'show_details', self.show_details)
        footer = AttrWrap(Text(" Q to exit"), "footer")
        rows, cols = raw_display.Screen().get_cols_rows()
        h = rows - 2
        f1 = Filler(self.list_view, valign='top', height=h)
        f2 = Filler(self.detail_view, valign='top')
        c_list = LineBox(f1, title="聊天", title_align='left')
        c_details = LineBox(f2, title="Country Details")
        columns = Columns([('weight', 30, c_list), ('weight', 70, c_details)])
        frame = AttrMap(Frame(body=columns, footer=footer), 'bg')
        self.loop = MainLoop(frame, self.palette, unhandled_input=self.unhandled_input)

    def update_data(self):
        data = []
        for _ in range(10):
            data.append({"name":"USA",     "pop":"325,084,756",   "gdp":"$ 19.485 trillion"})
            data.append({"name":"China",   "pop":"1,421,021,791", "gdp":"$ 12.238 trillion"})
            data.append({"name":"Japan",   "pop":"127,502,725",   "gdp":"$ 4.872 trillion"})
            data.append({"name":"Germany", "pop":"82,658,409",    "gdp":"$ 3.693 trillion"})
            data.append({"name":"India",   "pop":"1,338,676,785", "gdp":"$ 2.651 trillion"})

        self.list_view.set_data(data)

    def start(self):
        self.update_data()
        self.loop.run()
