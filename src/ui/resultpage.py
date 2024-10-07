from tkinter import ttk, StringVar, constants
from data.OPTIMIZEDnegmodel2withclass import DataModel


class ResultPage:

    def __init__(self, root, mainpage_view, direction, date, time, temperature, wind, precipitation):
        self._root = root
        self.window = None

        self.mainpage_view = mainpage_view

        self.direction_og = direction
        self.temperature_og = temperature
        self.wind_og = wind
        self.precipitation_og = precipitation

        if direction == "To Suomenlinna":
            self.direction = 99
        else:
            self.direction = 98

        self.date = date
        self.year = int(self.date[6:])
        self.month = int(self.date[3:5])
        self.day = int(self.date[:2])

        self.time = int(time)

        if temperature == "21 to 30 degrees":
            self.temperature = 25.5
        elif temperature == "11 to 20 degrees":
            self.temperature = 15.5
        elif temperature == "1 to 10 degrees":
            self.temperature = 5.5
        elif temperature == "0 to -9 degrees":
            self.temperature = -4.5
        elif temperature == "-10 to -19 degrees":
            self.temperature = -14.5
        else:
            self.temperature = -24.5
                
        if wind == "light wind":
            self.wind = 2.5
        elif wind == "moderate wind":
            self.wind = 7.5
        else:
            self.wind = 10

        if precipitation == "no rain/snow":
            self.precipitation = 0.0
        elif precipitation == "light rain":
            self.precipitation = 3.5
        elif precipitation == "moderate rain":
            self.precipitation = 10.5
        elif precipitation == "heavy rain":
            self.precipitation = 14
        elif precipitation == "light snow":
            self.precipitation = 3.5
        elif precipitation == "moderate snow":
            self.precipitation = 10.5
        else:
            self.precipitation = 14

        self.start()

    def start(self):
            
            
        self.model = DataModel(self._root, self.year, self.month, self.day, self.time, self.temperature, self.wind, self.precipitation, self.direction)
        self.prediction = self.model.predict_traffic()

        if self.prediction <= 80:
            self.result = "NOT BUSY"
            self.colour = "green"
        elif self.prediction <= 160:
            self.result = "MODERATELY BUSY"
            self.colour = "yellow"
        elif self.prediction <= 240:
            self.result = "QUITE BUSY"
            self.colour = "orange"
        elif self.prediction <= 320:
            self.result = "VERY BUSY"
            self.colour = "red"
        else:
            self.result = "EXTREMELY BUSY"
            self.colour = "dark red"

        self.show_result()

    def show_result(self):

        self.window = ttk.Frame(self._root)
        style = ttk.Style()

        heading = ttk.Label(self.window, text="Suomenlinna Ferry Traffic Predictor", font=("Helvetica", 26))
        heading.grid(padx=5, pady=50)

        heading2 = ttk.Label(self.window, text=f"Predicted ferry traffic:", font=("Helvetica", 16))
        heading2.grid(padx=5, pady=10)

        result = ttk.Label(self.window, text=f"{self.result}", font=("Helvetica", 26, "bold"), foreground=self.colour)
        result.grid(padx=5, pady=50)

        heading3 = ttk.Label(self.window, text=f"Prediction made for the following parameters:", font=("Helvetica", 16))
        heading3.grid(padx=5, pady=20)

        date = ttk.Label(self.window, text=f"Date: {self.date}", font=("Helvetica", 12))
        date.grid(padx=5, pady=10)

        time = ttk.Label(self.window, text=f"Hour: {self.time}:00", font=("Helvetica", 12))
        time.grid(padx=5, pady=10)

        temp = ttk.Label(self.window, text=f"Predicted temperature: {self.temperature_og}", font=("Helvetica", 12))
        temp.grid(padx=5, pady=10)

        wind = ttk.Label(self.window, text=f"Predicted wind: {self.wind_og}", font=("Helvetica", 12))
        wind.grid(padx=5, pady=10)

        precipitation = ttk.Label(self.window, text=f"Predicted precipitation: {self.precipitation_og}", font=("Helvetica", 12))
        precipitation.grid(padx=5, pady=10)

        back_button = ttk.Button(self.window, command=self.mainpage_view, text="Make another prediction")
        back_button.grid(column=0, padx=5, pady=50)

        self.window.pack()

        

    

    