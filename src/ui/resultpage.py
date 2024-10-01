from tkinter import ttk, StringVar, constants


class ResultPage:

    def __init__(self, root, direction, date, time, temperature, wind, precipitation):
        self._root = root
        self.window = None
        self.start()

    def start(self):
            
            self.window = ttk.Frame(self._root)
            style = ttk.Style()
    
            heading = ttk.Label(self.window, text="Suomenlinna Ferry Traffic Predictor", font=("Helvetica", 26))
            heading.grid(padx=5, pady=50)
    
            result = ttk.Label(self.window, text="Predicted ferry traffic: 1000 passengers", font=("Helvetica", 16))
            result.grid(padx=5, pady=10)

            self.window.pack()