import módulo2 as m2
from tkinter import *


def no_orb():
 window.destroy()
 m2.find_npc_duel_no_orb()
 
def npc():
 window.destroy()    
 m2.find_npc_duel()

def pvp():
 window.destroy()
 m2.pvp_duel()


window = Tk()

window.title("Duel_Bot")

window.geometry('100x250')

lbl = Label(window, text="Select Mode:")
lbl.grid(column=0, row=0)

btn = Button(window, text="NPC duel with no orbs", command = no_orb)
btn.grid(column=0, row=1)

btn2 = Button(window, text="NPC duel with orbs", command = npc)
btn2.grid(column=0, row=2)

btn3 = Button(window, text="PvP Duel", command = pvp)
btn3.grid(column=0, row=3)

 
window.mainloop()
