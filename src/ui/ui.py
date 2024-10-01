from ui.mainpage import MainPage
from ui.resultpage import ResultPage


class UI:

    def __init__(self,root):
        self._root = root
        self.window = None
        self.mainpage_view()

    def hide_current_view(self):
        if self.window:
            self.window.destroy()
            self.window = None

    def mainpage_view(self):
        self.hide_current_view()
        self.window = MainPage(self._root, self.resultpage_view)

    def resultpage_view(self, direction, date, time, temperature, wind, precipitation):
        self.hide_current_view()
        self.window = ResultPage(self._root, direction, date, time, temperature, wind, precipitation)