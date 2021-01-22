from tkinter import * 
from tkinter import messagebox

root = Tk()
root.geometry('534x507')
root.resizable(width=0,height=0)
root.title("Tic Tac Toe")

clicked = True
count = 0
winner = False

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def checkwon():
    global winner
    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        winner = True
        messagebox.showinfo(title='Tic Tac Toe',message="Congralations 'x' won!!!")
        disable_all_buttons()
    elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        winner = True
        messagebox.showinfo(title='Tic Tac Toe',message="Congralations 'x' won!!!")
        disable_all_buttons()


    elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
        b7.config(bg='red')
        b8.config(bg='red')
        b9.config(bg='red')
        winner = True
        messagebox.showinfo(title='Tic Tac Toe',message="Congralations 'x' won!!!")

    elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
        b1.config(bg='red')
        b4.config(bg='red')
        b7.config(bg='red')
        winner = True
        messagebox.showinfo(title='Tic Tac Toe',message="Congralations 'x' won!!!")
        disable_all_buttons()


    elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
        b5.config(bg='red')
        b2.config(bg='red')
        b8.config(bg='red')
        winner = True
        messagebox.showinfo(title='Tic Tac Toe',message="Congralations 'x' won!!!")
        disable_all_buttons()


    elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
        b3.config(bg='red')
        b6.config(bg='red')
        b9.config(bg='red')    
        winner = True
        messagebox.showinfo(title='Tic Tac Toe',message="Congralations 'x' won!!!")
        disable_all_buttons()


    elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
        b1.config(bg='red')
        b5.config(bg='red')
        b9.config(bg='red') 
        messagebox.showinfo(title='Tic Tac Toe',message="Congralations 'x' won!!!")       
        disable_all_buttons()

    elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
        b3.config(bg='red')
        b5.config(bg='red')
        b7.config(bg='red') 
        messagebox.showinfo(title='Tic Tac Toe',message="Congralations 'x' won!!!")   
        disable_all_buttons()

    elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        winner = True
        messagebox.showinfo(title='Tic Tac Toe',message="Congralations 'O' won!!!")
        disable_all_buttons()
    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
        b4.config(bg='green')
        b5.config(bg='green')
        b6.config(bg='green')
        winner = True
        messagebox.showinfo(title='Tic Tac Toe',message="Congralations 'O' won!!!")
        disable_all_buttons()


    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
        b7.config(bg='green')
        b8.config(bg='green')
        b9.config(bg='green')
        winner = True
        messagebox.showinfo(title='Tic Tac Toe',message="Congralations 'O' won!!!")

    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        winner = True
        messagebox.showinfo(title='Tic Tac Toe',message="Congralations 'O' won!!!")
        disable_all_buttons()


    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        b5.config(bg='green')
        b2.config(bg='green')
        b8.config(bg='green')
        winner = True
        messagebox.showinfo(title='Tic Tac Toe',message="Congralations 'O' won!!!")
        disable_all_buttons()


    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
        b3.config(bg='green')
        b6.config(bg='green')
        b9.config(bg='green')    
        winner = True
        messagebox.showinfo(title='Tic Tac Toe',message="Congralations 'O' won!!!")
        disable_all_buttons()


    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        b1.config(bg='green')
        b5.config(bg='green')
        b9.config(bg='green') 
        messagebox.showinfo(title='Tic Tac Toe',message="Congralations 'O' won!!!")       
        disable_all_buttons()

    elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
        b3.config(bg='green')
        b5.config(bg='green')
        b7.config(bg='green') 
        messagebox.showinfo(title='Tic Tac Toe',message="Congralations 'O' won!!!")   
        disable_all_buttons()    
    else:
        if count == 9 and winner == False:
            messagebox.showinfo(title='Tic Tac Toe',message="It's a Tie")
            disable_all_buttons()
def but_click(value):
    global clicked,count
    
    if value['text'] == " " and clicked==True:
        count +=1
        value['text'] = "X"
        clicked = False
        checkwon()
    elif value['text'] == " " and clicked==False:
        count +=1
        value['text'] = "O"
        clicked = True   
        checkwon() 
    else:
        messagebox.showerror("Tic Tac Toe","That box has already been selected")  

      
def reset():  
    defaultbg = root.cget('bg')
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked,count
    clicked = True
    count = 0
    b1 = Button(root,text=" ",justify=CENTER,font=('Arial',20),command=lambda:but_click(b1),width=10,height=5,bg=defaultbg)
    b2 = Button(root,text=" ",justify=CENTER,font=('Arial',20),command=lambda:but_click(b2),width=10,height=5,bg=defaultbg)
    b3 = Button(root,text=" ",justify=CENTER,font=('Arial',20),command=lambda:but_click(b3),width=10,height=5,bg=defaultbg)
    b4 = Button(root,text=" ",justify=CENTER,font=('Arial',20),command=lambda:but_click(b4),width=10,height=5,bg=defaultbg)
    b5 = Button(root,text=" ",justify=CENTER,font=('Arial',20),command=lambda:but_click(b5),width=10,height=5,bg=defaultbg)
    b6 = Button(root,text=" ",justify=CENTER,font=('Arial',20),command=lambda:but_click(b6),width=10,height=5,bg=defaultbg)
    b7 = Button(root,text=" ",justify=CENTER,font=('Arial',20),command=lambda:but_click(b7),width=10,height=5,bg=defaultbg)
    b8 = Button(root,text=" ",justify=CENTER,font=('Arial',20),command=lambda:but_click(b8),width=10,height=5,bg=defaultbg)
    b9 = Button(root,text=" ",justify=CENTER,font=('Arial',20),command=lambda:but_click(b9),width=10,height=5,bg=defaultbg)

    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)
    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)
    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)

my_menu = Menu(root)
root.config(menu=my_menu)

options_menu = Menu(my_menu,tearoff= False)
my_menu.add_cascade(label="options",menu=options_menu)
options_menu.add_command(label='reset',command=reset)
reset()
root.mainloop()



    