#Load Tk library
from tkinter import *
#Load themed widgets
from tkinter import ttk

#PhotoImage() imports picture files
#after() is a tkinter friendly delay
#python list is a good way to store the numbers
#	list.remove("xyz") is a good way to remove from list
#	random.choice(myList) is a way to pick the number

   
#-------START raffle settings menu-------
root = Tk()
root.title("OLOW Raffle")

#minimize the root window
root.wm_state('iconic')

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

#create and configure settings window
settingsmenu=Toplevel()
settingsmenu.title("Raffle Settings")
settingsframe = ttk.Frame(settingsmenu, padding="3 3 12 12")
settingsframe.grid(column=0, row=0, sticky=(N, W, E, S))

#declare input ticket variable
totaltickets = IntVar()
#declare input sponsor variable
sponsordir = StringVar()

#create tickets sold label
ttk.Label(settingsframe, text="Total Tickets Sold:").grid(column=0, row=0, sticky=(W, E))

#get number of tickets sold
tickets_entry = ttk.Entry(settingsframe, width=7, textvariable=totaltickets)
#config entry
tickets_entry.grid(column=1, row=0, sticky=(W, E))

#create running time label
ttk.Label(settingsframe, text="Total Running Time:").grid(column=0, row=1, sticky=(W, E))

#create drop down menu
run_time = IntVar()
choices = [1,1,15,30,45,60,75,90,105,120,135,150]
ttk.OptionMenu(settingsframe, run_time, *choices).grid(column=1, row=1, sticky=(W,E))

#create minutes label
ttk.Label(settingsframe, text="minutes").grid(column=2, row=1, sticky=(W, E))

#create sponsor folder label
ttk.Label(settingsframe, text="Sponsor Folder:").grid(column=0, row=3, sticky=(W, E))

#get sponsor folder location
sponsors_entry = ttk.Entry(settingsframe, width=7, textvariable=sponsordir)
#config entry
sponsors_entry.grid(column=1, row=3, sticky=(W, E))

def find_winner():
	#create list
	#pick random number from list: random.choice(myList)
	#remove number from list: list.remove(number)
	#find column of the picked number
	ggg = 23
	#find row of picked number
	#remove number from main window
	##ttk.Label(mainframe, text=" ").grid(column=0, row=0)
	ttk.Label(mainframe, text=(ggg)).grid(column=0, row=0)
	#loop it totaltickets-1 times

def set_settings():
	count = 1
	
	#minimize the settings window
	settingsmenu.wm_state('iconic')
	#maximize the main window
	root.wm_state('normal')
	
	for x in range(0,20):
		for y in range(0,20):
			if(count <= totaltickets.get()):
				ttk.Label(mainframe, text=(count)).grid(column=y, row=x)
				count=count+1


	root.after(2000, find_winner)
#def find_winner():
	#get random num b/w 1 and totaltickets.get()
	#

#create start button
ttk.Button(settingsframe, text="GO!", command=set_settings).grid(column=1, row=2)

root.mainloop()
