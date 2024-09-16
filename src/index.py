from tkinter import Tk
from mainpage import MainPage

def main():
    window = Tk()
    window.title("Suomenlinna Ferry Traffic Predictor")
    window.geometry("1200x1000")
    MainPage(window)

    window.mainloop()

if __name__ == "__main__":
    main()