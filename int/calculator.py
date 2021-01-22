from tkinter import *
import math as m

root = Tk()
root.resizable(width="0",height="0")
root.title("Calculator")
entry = Entry(root,width=50,fg="black",borderwidth=5,relief=RIDGE,font=("Calibri",12))
entry.grid(row=0,column=0,padx=1,pady=10,ipady=10,columnspan=5)

def click(value):
    old = entry.get()
    entry.delete(0,END)
    entry.insert(0,old+value)
    return

def clear():
    entry.delete(0,END)
    return

def bksp():
    old = entry.get()
    val = len(old)-1
    entry.delete(val,END)
    return
    
def evaluate():
    old = entry.get()
    val = eval(old)
    entry.delete(0,END)
    entry.insert(0,val)    

def sc(text):
    num = entry.get()
    result = ''
    if text == "deg":
        result =str(m.degrees(float(num)))
    if text == "sin":
        result =str(m.sin(float(num)))
    if text == "cos":
        result =str(m.cos(float(num)))
    if text == "tan":
        result =str(m.tan(float(num)))        
    if text == "lg":
        result = str(m.log10(float(num)))    
    if text == "ln":
        result =str(m.log(float(num))) 
    if text == "sqrt":
        result =str(m.sqrt(float(num))) 
    if text == "cbrt":
        result = str(float(num)**(1/3))
    if text == "x!":
        result =str(m.factorial(float(num)))   
    if text == "1/x":
        result =str(1/(float(num))) 
    if text == "pi":
        if num == "":
            result = str(m.pi)
        else:
            result = str(float(num)*m.pi) 
    if text == "e":
        if num == "":
            result = str(m.e)
        else:
            result = str(m.e**float(num))       
    entry.delete(0,END)
    entry.insert(0,result)                  

log = Button(root,text="lg",padx=39,pady=20,command=lambda :sc("lg"))
log.grid(row=1,column=0)

ln = Button(root,text="ln",padx=40,pady=20,command=lambda :sc("ln"))
ln.grid(row=1,column=1)

par1 = Button(root,text="(",padx=40,pady=20,command=lambda:click("("))
par1.grid(row=1,column=2)

par2 = Button(root,text=")",padx=40,pady=20,command=lambda:click(")"))
par2.grid(row=1,column=3)

dot = Button(root,text=".",padx=40,pady=20,command=lambda:click("."))
dot.grid(row=1,column=4)

cbrt = Button(root,text="cbrt",padx=33,pady=20,command=lambda :sc("cbrt"))
cbrt.grid(row=2,column=0)

deg = Button(root,text="deg",padx=35,pady=20,command=lambda :sc("deg"))
deg.grid(row=2,column=1)

sin = Button(root,text="sin",padx=34,pady=20,command=lambda :sc("sin"))
sin.grid(row=2,column=2)

cos = Button(root,text="cos",padx=32,pady=20,command=lambda :sc("cos"))
cos.grid(row=2,column=3)

tan = Button(root,text="tan",padx=32,pady=20,command=lambda :sc("tan"))
tan.grid(row=2,column=4)

sqrt = Button(root,text="sqrt",padx=33,pady=20,command=lambda :sc("sqrt"))
sqrt.grid(row=3,column=0)

clr = Button(root,text="clr",padx=38,pady=20,bg="red",fg="white",command=lambda :clear())
clr.grid(row=3,column=1)

bksp = Button(root,text="bksp",padx=28,pady=20,bg="red",fg="white",command=bksp)
bksp.grid(row=3,column=2)

mod = Button(root,text="mod",padx=28,pady=20,command=lambda:click("%"))
mod.grid(row=3,column=3)

backslash = Button(root,text="/",padx=40,pady=20,command=lambda:click("/"))
backslash.grid(row=3,column=4)

fact = Button(root,text="x!",padx=39,pady=20,command=lambda :sc("x!"))
fact.grid(row=4,column=0)

seven = Button(root,text="7",padx=40,pady=20,command=lambda:click("7"))
seven.grid(row=4,column=1)

eight = Button(root,text="8",padx=40,pady=20,command=lambda:click("8"))
eight.grid(row=4,column=2)

nine = Button(root,text="9",padx=40,pady=20,command=lambda:click("9"))
nine.grid(row=4,column=3)

mul = Button(root,text="*",padx=40,pady=20,command=lambda:click("*"))
mul.grid(row=4,column=4)

ilo = Button(root,text="1/x",padx=35.5,pady=20,command=lambda :sc("1/x"))
ilo.grid(row=5,column=0)

four = Button(root,text="4",padx=40,pady=20,command=lambda:click("4"))
four.grid(row=5,column=1)

five = Button(root,text="5",padx=40,pady=20,command=lambda:click("5"))
five.grid(row=5,column=2)

six = Button(root,text="6",padx=40,pady=20,command=lambda:click("6"))
six.grid(row=5,column=3)

sub = Button(root,padx=41,pady=20,text="-",command=lambda:click("-"))
sub.grid(row=5,column=4)

pi = Button(root,text="pi",padx=39.5,pady=20,command=lambda :sc("pi"))
pi.grid(row=6,column=0)

three = Button(root,text="3",padx=40,pady=20,command=lambda:click("3"))
three.grid(row=6,column=1)

two = Button(root,text="2",padx=40,pady=20,command=lambda:click("2"))
two.grid(row=6,column=2)

one = Button(root,text="1",padx=40,pady=20,command=lambda:click("1"))
one.grid(row=6,column=3)

add = Button(root,text="+",padx=38,pady=20,command=lambda:click("+"))
add.grid(row=6,column=4)

exp = Button(root,text="e",padx=40,pady=20,command=lambda :sc("exp"))
exp.grid(row=7,column=1)

zero = Button(root,text="0",padx=40,pady=20,command=lambda:click("0"))
zero.grid(row=7,column=2)

eql = Button(root,text="=",padx=38,pady=20,command=evaluate)
eql.grid(row=7,column=3)

root.mainloop()