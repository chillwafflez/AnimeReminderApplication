from win10toast import ToastNotifier
from datetime import datetime
from datetime import date
import schedule
import time
from fetchMethods import *


def notify(name, timeLeft):
    toaster = ToastNotifier()
    if (timeLeft == "1"):
        toaster.show_toast(name + " is airing in " + timeLeft + " hour.", duration=6)
    if (timeLeft == "now"):
        toaster.show_toast(name + " is airing now!", duration=6)
    print("reached the end")

notify("Vinland Saga", "now")


