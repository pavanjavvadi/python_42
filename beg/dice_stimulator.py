import tkinter as tk
import random

root = tk.Tk()
root.geometry('800x800')
label = tk.Label(root,font=('times',200))
def roll():
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.config(text=f'{random.choice(number)}')
    label.pack()
button = tk.Button(root,text="roll",command=roll )
button.place(x=375,y=10)
root.mainloop()