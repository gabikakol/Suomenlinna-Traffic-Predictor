from tkinter import Tk
from ui.mainpage import MainPage
from ui.resultpage import ResultPage

#from data.negmodel2withclass import DataModel


class UI:

    def __init__(self,root):    
        self._root = root
        self._window = None
        self.mainpage_view()

    def hide_current_view(self):
        if self._window:
            self._root.destroy()
            self._root = Tk()
            self._root.title("Suomenlinna Ferry Traffic Predictor")
            self._root.geometry("1200x1000")
            self._window = None

    def mainpage_view(self):
        self.hide_current_view()
        self._window = MainPage(self._root, self.resultpage_view)

    def resultpage_view(self, direction, date, time, temperature, wind, precipitation):
        self.hide_current_view()
        self._window = ResultPage(self._root, direction, date, time, temperature, wind, precipitation)