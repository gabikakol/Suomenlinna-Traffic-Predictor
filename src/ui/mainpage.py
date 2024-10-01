from tkinter import ttk, StringVar, PhotoImage
from tkcalendar import Calendar
import datetime

class MainPage:

    def __init__(self, root, resultpage_view):
        self._root = root
        self.window = None 
        self.resultpage_view = resultpage_view
        self.start()

    def start(self):

        self.window = ttk.Frame(self._root)
        style = ttk.Style()

        heading = ttk.Label(self.window, text="Suomenlinna Ferry Traffic Predictor", font=("Helvetica", 26))
        heading.grid(padx=5, pady=50)

        direction = ttk.Label(self.window, text="Direction", font=("Helvetica", 16))
        direction.grid(column=0, padx=5, pady=10)

        direction_options = ['To Suomenlinna', 'From Suomenlinna']
        self.dir_var = StringVar(self._root)
        direction_menu = ttk.Combobox(self.window, textvariable=self.dir_var, values=direction_options, width=20)
        direction_menu['values'] = direction_options
        direction_menu.grid(pady=10) 
        direction_menu.current(0)

        date = ttk.Label(self.window, text="Date", font=("Helvetica", 16))
        date.grid(column=0, padx=5, pady=10)

        #edit the funtion to set minimum date to current date
        self.cal = Calendar(self.window, mindate=datetime.date.today(), maxdate=datetime.date(2026, 1, 1))
        self.cal.grid(padx=5, pady=10)

        time = ttk.Label(self.window, text="Time (full hour)", font=("Helvetica", 16))
        time.grid(column=0, padx=5, pady=10)

        self.hour_var = StringVar(value='0')  # default value is '0'
        hours = [str(hour) for hour in range(24) if hour not in (3, 4, 5)]
        hour_spinbox = ttk.Spinbox(self.window, values=hours, textvariable=self.hour_var, wrap=True, width=10)
        hour_spinbox.grid(column=0, padx=5, pady=10)

        weather = ttk.Label(self.window, text="Expected weather", font=("Helvetica", 16))
        weather.grid(column=0, padx=5, pady=10)

        temp = ttk.Label(self.window, text="1. Temperature", font=("Helvetica", 12))
        temp.grid(column=0, padx=5, pady=10)

        temp_options = ["21 to 30 degrees", "11 to 20 degrees", "1 to 10 degrees", "0 to -9 degrees", "-10 to -19 degrees", "-20 to -30 degrees"]
        self.temp_var = StringVar(self._root)
        temp_menu = ttk.Combobox(self.window, textvariable=self.temp_var, values=direction_options, width=20)
        temp_menu['values'] = temp_options
        temp_menu.grid(pady=10) 
        temp_menu.current(0)

        wind = ttk.Label(self.window, text="2. Wind", font=("Helvetica", 12))
        wind.grid(column=0, padx=5, pady=10)

        wind_options = ["light wind", "moderate wind", "heavy wind"]
        self.wind_var = StringVar(self._root)
        wind_menu = ttk.Combobox(self.window, textvariable=self.wind_var, values=direction_options, width=20)
        wind_menu['values'] = wind_options
        wind_menu.grid(pady=10)
        wind_menu.current(0)

        rain = ttk.Label(self.window, text="3. Precipitation", font=("Helvetica", 12))
        rain.grid(column=0, padx=5, pady=10)

        rain_options = ["no rain/snow", "light rain", "moderate rain", "heavy rain", "light snow", "moderate snow", "heavy snow"]
        self.rain_var = StringVar(self._root)
        rain_menu = ttk.Combobox(self.window, textvariable=self.rain_var, values=direction_options, width=20)
        rain_menu['values'] = rain_options
        rain_menu.grid(pady=10)
        rain_menu.current(0)

        save_button = ttk.Button(self.window, command=self.handle_prediction, text="Predict the traffic")
        save_button.grid(column=0, padx=5, pady=10)

        self.window.pack()

    def handle_prediction(self):
        direction = self.dir_var.get()
        date = self.cal.get_date()
        time = self.hour_var.get()
        temperature = self.temp_var.get()
        wind = self.wind_var.get()
        precipitation = self.rain_var.get()
        self.resultpage_view(direction, date, time, temperature, wind, precipitation)

