from win10toast import ToastNotifier
from datetime import datetime
from datetime import date
import schedule
import time
from fetchMethods import *


animeListNAMES = []

def fuck_you():
    print("fuck you")

def meow():
    print("meow")

def main():
    schedule.every().day.at("00:00").do(fuck_you).tag('anime')
    schedule.every().day.at("00:00").do(fuck_you).tag('anime')
    schedule.every().day.at("00:00").do(meow)

if __name__ == "__main__":
    main()

print(schedule.get_jobs())
schedule.clear('anime')
print('got rid of anime jobs')
print(schedule.get_jobs())




