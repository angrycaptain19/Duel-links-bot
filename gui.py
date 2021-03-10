import módulo2 as m2
from tkinter import *
import ctypes


window = Tk()

window.title("Duel_Bot")

window.geometry('100x250')

lbl = Label(window, text="Select Mode:")
lbl.grid(column=0, row=0)

btn = Button(window, text="NPC duel with no orbs", command = m2.find_npc_duel_no_orb)
btn.grid(column=0, row=1)

btn2 = Button(window, text="NPC duel with orbs", command = m2.find_npc_duel)
btn2.grid(column=0, row=2)

btn3 = Button(window, text="PvP Duel", command = m2.find_npc_duel)
btn3.grid(column=0, row=3)

 
window.mainloop()
