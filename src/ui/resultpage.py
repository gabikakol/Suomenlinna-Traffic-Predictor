from tkinter import ttk, StringVar, constants


class ResultPage:

    def __init__(self, root, direction, date, time, temperature, wind, precipitation):
        self._root = root
        self.window = None
        self.resultpage_view()
