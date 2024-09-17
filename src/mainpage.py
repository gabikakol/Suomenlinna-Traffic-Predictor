from tkinter import ttk, StringVar, constants
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

        heading = ttk.Label(self.window, text="Suomenlinna Ferry Traffic Predictor", font=("Helvetica", 36))
        heading.grid(padx=5, pady=100)

        direction = ttk.Label(self.window, text="Direction", font=("Helvetica", 16))
        direction.grid(column=0, padx=5, pady=10)

        direction_options = ['To Suomenlinna', 'From Suomenlinna']
        self.dir_var = StringVar(self._root)
        direction_menu = ttk.Combobox(self.window, textvariable=self.dir_var, values=direction_options, width=20)
        direction_menu['values'] = direction_options
        direction_menu.grid(pady=10) 
        direction_menu.current(0)
        """
        OptionMenu(
            self.window, self.dir_var, *direction_options, style="dir.TButton")
        direction_menu.grid(row=2, column=0, padx=5, pady=5, sticky=constants.EW)
        """

        date = ttk.Label(self.window, text="Date", font=("Helvetica", 16))
        date.grid(column=0, padx=5, pady=10)

        #edit the funtion to set minimum date to current date
        self.cal = Calendar(self.window, mindate=datetime.date.today(), maxdate=datetime.date(2025, 1, 1))
        self.cal.grid(padx=5, pady=10)

        """
        # Button that saves the selected date
        save_cal_button = ttk.Button(self.window, text="Save date", command=self.select_date)
        save_cal_button.grid(row=5, column=0, padx=5, pady=5)
        """

        time = ttk.Label(self.window, text="Time (full hour)", font=("Helvetica", 16))
        time.grid(column=0, padx=5, pady=10)

        self.hour_var = StringVar(value='0')  # default value is '0'
        hour_spinbox = ttk.Spinbox(self.window, from_=0, to=23, textvariable=self.hour_var, wrap=True, width=10)
        hour_spinbox.grid(column=0, padx=5, pady=10)

        save_button = ttk.Button(self.window, text="Predict the traffic")
        save_button.grid(column=0, padx=5, pady=10)

        self.window.pack()


""" 
    def select_date(self):
        # Fetch the selected date from the calendar
        selected_date = self.cal.get_date()
        # Print the selected date to the console
        print("Selected Date:", selected_date)
"""