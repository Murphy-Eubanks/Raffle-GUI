import sys
import tkinter
from tkinter import ttk

root = Tk()
root.title("Raffle")

mainframe = ttk.Frame(root, padding='3 3 10 10')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

def grid():
	gnum = ttk.Entry(mainframe, width=5)
	



tk.mainloop()
