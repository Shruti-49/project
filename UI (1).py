# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 22:01:25 2021

@author: Admin
"""

import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import os
import webbrowser

from motiondetector import motion
def Ok():
    uname = e1.get()
    password = e2.get()
 
    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")
 
 
    elif(uname == "Admin" and password == "Minorpro6"):
 
        messagebox.showinfo("","Login Success")
        path=r'C:\Users\HP\Desktop\projectfinal\recordings'
        webbrowser.open(os.path.realpath(path))
        root.destroy()
        return
 
    else :
        messagebox.showinfo("","Incorrect Username or Password")
 
 

def openfolder():         
    root = Tk()
    root.title("Login")
    root.geometry("300x200")
    global e1
    global e2
     
    Label(root, text="User ID", font=('Verdana',12)).place(x=10, y=10)
    Label(root, text="Password", font=('Verdana',12)).place(x=10, y=40)
     
    e1 = Entry(root)
    e1.place(x=140, y=10)
     
    e2 = Entry(root)
    e2.place(x=140, y=40)
    e2.config(show="*")    
     
    Button(root, text="Login", command=Ok, bg="navy blue", fg="white", font=('Verdana',12), height = 2, width = 20).place(x=10, y=100)
    
    
class App:
    def __init__(self,master):
        global passg
        title="Always Vigilant"       
        msgtitle=Message(master,text=title)
        msgtitle.config(font=('Verdana',20),width=400)
       
        msgtitle.pack()       
        msgtitle.pack(padx=5, pady=30)

        self.encrypt = Button(master,text="Start Surveillance",bg="navy blue", fg="white",command=motion, font=('Verdana',12), width=25,height=2)
        self.encrypt.pack(side=LEFT,padx=5, pady=5)
        self.decrypt = Button(master,text="View Previous recordings",bg="navy blue", fg="white",command=openfolder,font=('Verdana',12), width=25,height=2)
        self.decrypt.pack(side=RIGHT,padx=5, pady=5)



root=Tk()
root.wm_title("Suspicious Activity Detection")
app=App(root)

root.mainloop()
