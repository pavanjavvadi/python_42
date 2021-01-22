import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x300")
root.resizable(width=0,height=0)
root.title("Time Counter")

# Declaration of variables
hour=StringVar()
minute=StringVar()
second=StringVar()

# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")

hourEntry= Entry(root, width=5,textvariable=hour,justify=CENTER)
hourEntry.place(x=100,y=100)
minuteEntry= Entry(root, width=5, justify=CENTER,textvariable=minute)
minuteEntry.place(x=140,y=100)
secondEntry= Entry(root, width=5, justify=CENTER,textvariable=second)
secondEntry.place(x=180,y=100)

def submit():
	try:
		temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
	except:
		print("Please input the right value")
	while temp >-1:		
		mins,secs = divmod(temp,60) 
		hours=0
		if mins >60:
			hours, mins = divmod(mins, 60)
		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))
		root.update()
		time.sleep(1)
		if (temp == 0):
			messagebox.showinfo("Time Countdown", "Time's up ")   
		temp -= 1

def stop():
    hours = hour.get()
    mins = minute.get()
    secs = second.get()
    hour.set("{0:2d}".format(hours))
    minute.set("{0:2d}".format(mins))
    second.set("{0:2d}".format(secs))

btn = Button(root, text='Start', bd='5',command= submit, bg="green")
btn.place(x=90,y=130)
btn2 = Button(root,text="Stop",bd="5",command = stop,bg="red")
btn2.place(x=160,y=130)
root.mainloop()
 





 def alarm():
    global e1,e2
    window = Toplevel()
    window.title("Alarm")
    hours = Label(window,text="Hours:").grid(row=1,column=1)
    e1 = Entry(window,justify=CENTER).grid(row=1,column=2)
    minutes = Label(window,text="Minutes:").grid(row=2,column=1)
    e2 = Entry(window,justify=CENTER).grid(row=2,column=2)
    button = Button(window,text="set alarm",bg="green",command=lambda : ring_alarm())
    button.grid(row=3,column=1)