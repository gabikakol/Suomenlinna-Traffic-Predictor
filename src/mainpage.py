from tkinter import ttk, StringVar, constants

class MainPage:

    def __init__(self, root):
        self._root = root
        self.window = None
        self.mainpage_view()

    def hide_current_view(self):
        if self.window:
            self.window.destroy()
            self.window = None

    def mainpage_view(self):
        self.hide_current_view()
        self.window = ttk.Frame(self._root)

        heading = ttk.Label(self.window, text="Suomenlinna Ferry Traffic Predictor", font=("Helvetica", 36))
        heading.grid(padx=5, pady=100, column=1)

        self.window.pack()