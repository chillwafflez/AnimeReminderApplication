from tkinter import *
from tkinter import ttk
from fetchMethods import *
from datetime import datetime
import time

root = Tk()

root.geometry("500x500")


def showAirDate():
    data = getNextEpisode("Vinland Saga Season 2")
    airingAt = data['data']['Media']['nextAiringEpisode']['airingAt']
    t = time.ctime(airingAt)

    msg = "Vinland Saga episode is airing on " + t
    top = Toplevel(root)
    top.geometry("500x200")
    top.title("Air Date")
    #Label(top, text="Vinland Saga airs at" + airingAt).place(x=150,y=80)
    Label(top, text = msg).place(x=150,y=80)


ttk.Button(root, text= "Open", command= showAirDate).pack()
root.mainloop()