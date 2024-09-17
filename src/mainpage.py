from tkinter import ttk, StringVar, PhotoImage
from tkcalendar import Calendar
import datetime

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

        style = ttk.Style()

        self.hide_current_view()
        self.window = ttk.Frame(self._root)

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
        self.cal = Calendar(self.window, mindate=datetime.date.today(), maxdate=datetime.date(2025, 1, 1))
        self.cal.grid(padx=5, pady=10)

        time = ttk.Label(self.window, text="Time (full hour)", font=("Helvetica", 16))
        time.grid(column=0, padx=5, pady=10)

        self.hour_var = StringVar(value='0')  # default value is '0'
        hour_spinbox = ttk.Spinbox(self.window, from_=0, to=23, textvariable=self.hour_var, wrap=True, width=10)
        hour_spinbox.grid(column=0, padx=5, pady=10)

        weather = ttk.Label(self.window, text="Expected weather", font=("Helvetica", 16))
        weather.grid(column=0, padx=5, pady=10)

        temp = ttk.Label(self.window, text="1. Temperature", font=("Helvetica", 12))
        temp.grid(column=0, padx=5, pady=10)

        temp_options = ["30 to 21 degrees", "20 to 11 degrees", "10 to 1 degrees", "0 to -9 degrees", "-10 to -19 degrees", "-20 to -30 degrees"]
        self.temp_var = StringVar(self._root)
        temp_menu = ttk.Combobox(self.window, textvariable=self.temp_var, values=direction_options, width=20)
        temp_menu['values'] = temp_options
        temp_menu.grid(pady=10) 
        temp_menu.current(0)

        wind = ttk.Label(self.window, text="2. Wind", font=("Helvetica", 12))
        wind.grid(column=0, padx=5, pady=10)

        wind_options = ["no wind", "light wind", "moderate wind", "heavy wind"]
        self.wind_var = StringVar(self._root)
        wind_menu = ttk.Combobox(self.window, textvariable=self.wind_var, values=direction_options, width=20)
        wind_menu['values'] = wind_options
        wind_menu.grid(pady=10)
        wind_menu.current(0)

        rain = ttk.Label(self.window, text="3. Rainfall", font=("Helvetica", 12))
        rain.grid(column=0, padx=5, pady=10)

        rain_options = ["no rain", "light rain", "moderate rain", "heavy rain"]
        self.rain_var = StringVar(self._root)
        rain_menu = ttk.Combobox(self.window, textvariable=self.rain_var, values=direction_options, width=20)
        rain_menu['values'] = rain_options
        rain_menu.grid(pady=10)
        rain_menu.current(0)

        save_button = ttk.Button(self.window, text="Predict the traffic")
        save_button.grid(column=0, padx=5, pady=10)

        self.window.pack()