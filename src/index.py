from tkinter import Tk
from ui.ui import UI

def main():
    window = Tk()
    window.title("Suomenlinna Ferry Traffic Predictor")
    window.geometry("1200x1000")
    UI(window)

    window.mainloop()

if __name__ == "__main__":
    main()