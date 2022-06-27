from cgitb import text
from tkinter import *
from tkinter.tix import COLUMN
from turtle import width
from unittest import result


root = Tk()
root.title("calculator")

new_lebal = Label(root,text = """          let 
        have
        fun 
        with 
    calculator""" ,  font=("ALGERIAN",30),padx=50,pady=50,background="red",foreground="white")

new_lebal.grid(row =1,column=8,rowspan=3)


lebal = Label(root,  font=("ALGERIAN",50),background="yellow")
lebal.grid(row=0,column=0,columnspan=5)

statement = ""

def click(num):
    global statement
    statement += num
    lebal.config(text= statement)
def clear():
    global statement
    statement = ""
    lebal.config(text= statement)   
def calculate():
    global statement
    result =""
    if statement != "":
        try:
            result=eval(statement)
            
        except:
            result="error"
            statement = ""
    
        
    lebal.config(text=result) 
    

def delete():
    global statement
    v = len(statement)
    new =""
    for i in range(0,v-1):
        f = statement[i]
        new += f
        
    statement = new
        
    lebal.config(text=new)    
   
                 
                
    
    

button_1=Button(root,text="1",font = ("ALGERIAN",50),background="#ff9999", padx=50,pady=25,command=lambda:click("1"))
button_2=Button(root,text="2",font = ("ALGERIAN",50),background="#ff9999",padx=50,pady=25,command=lambda:click("2"))
button_3=Button(root,text="3",font = ("ALGERIAN",50),background="#ff9999",padx=50,pady=25,command=lambda:click("3"))
button_4=Button(root,text="4",font = ("ALGERIAN",50),background="#ff9999",padx=50,pady=25,command=lambda:click("4"))
button_5=Button(root,text="5",font = ("ALGERIAN",50),background="#ff9999",padx=50,pady=25,command=lambda:click("5"))
button_6=Button(root,text="6",font = ("ALGERIAN",50),background="#ff9999",padx=50,pady=25,command=lambda:click("6"))
button_7=Button(root,text="7",font = ("ALGERIAN",50),background="#ff9999",padx=50,pady=25,command=lambda:click("7"))
button_8=Button(root,text="8",font = ("ALGERIAN",50),background="#ff9999",padx=50,pady=25,command=lambda:click("8"))
button_9=Button(root,text="9",font = ("ALGERIAN",50),background="#ff9999",padx=50,pady=25,command=lambda:click("9"))
button_0=Button(root,text="0",font = ("ALGERIAN",50),background="#ff9999",padx=50,pady=25,command=lambda:click("0"))

button_add=Button(root,text="+",font = ("ALGERIAN",50),background="#ff9999",padx=46,pady=25,command = lambda:click("+"))
button_sub=Button(root,text="-",font = ("ALGERIAN",50),background="#ff9999",padx=54,pady=25,command=lambda:click("-"))

button_clear=Button(root,text="AC",font = ("ALGERIAN",50),background="#ff9999",padx=25,pady=25,command=lambda:clear())
button_equal=Button(root,text="=",font = ("ALGERIAN",50),background="#ff9999",padx=50,pady=25,command=lambda:calculate())

button_multi=Button(root,text="*",font = ("ALGERIAN",50),background="#ff9999",padx=54,pady=25,command=lambda:click("*"))
button_div=Button(root,text="/",font = ("ALGERIAN",50),background="#ff9999",padx=52,pady=25,command=lambda:click("/"))


button_power=Button(root,text="**",font = ("ALGERIAN",50),background="#ff9999",padx=45,pady=25,command = lambda:click("**"))
button_dot=Button(root,text=".",font = ("ALGERIAN",50),background="#ff9999",padx=60,pady=25,command=lambda:click("."))

button_del=Button(root,text="del",font = ("ALGERIAN",50),background="#ff9999",padx=7,pady=25,command=lambda:delete())


button_bracket1=Button(root,text="(",font = ("ALGERIAN",50),background="#ff9999",padx=50,pady=25,command=lambda:click("("))
button_bracket2=Button(root,text=")",font = ("ALGERIAN",50),background="#ff9999",padx=50,pady=25,command=lambda:click(")"))

button_7.grid(row=1,column=2)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=0)

button_4.grid(row=2,column=2)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=0)

button_3.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_1.grid(row=3,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=1,column=3)
button_clear.grid(row=4,column=2)

button_sub.grid(row=2,column=3)
button_multi.grid(row=3,column=3)
button_div.grid(row=3,column=4)

button_equal.grid(row=4,column=1)

button_dot.grid(row=1,column=4)
button_power.grid(row=2,column=4)

button_del.grid(row=4,column=3)

button_bracket1.grid(row=4,column=4)
button_bracket2.grid(row=4,column=5)


root.mainloop()