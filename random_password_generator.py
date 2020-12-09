import pickle as pi
import tkinter as tk
from tkinter import ttk
import string
import pandas as pd
import os

window=tk.Tk()
window.geometry("600x300")
window.title("**ViSpY**")

global var1 
var1=tk.IntVar()

#for generating random numbers
def prng():
    if os.path.exists("prng.dat")==True:
        if os.path.getsize("prng.dat")!=0:
            f=open("prng.dat","rb")
            n=pi.load(f)
            f.close()
            seed=n
        else:
            seed=9856523498371
    else:
        seed=9856523498371
    t=[]
    for i in range(985):
        seed=((5*seed)+17)%1213
        t.append(seed)
    f=open("prng.dat","wb")
    pi.dump(seed,f)
    f.close()
    return t
    
#for generating password
def password_generator(name):
    t=prng()
    upr_case=string.ascii_uppercase
    lwr_case=string.ascii_lowercase
    dgts=string.digits
    normal = string.ascii_uppercase + string.ascii_lowercase + string.digits
    symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
    chars= normal + symbols
    password1 = ''
    j=int(name/2)
    k=int(name/1.653)
    for i in range(name-4):
        t[i]=t[i]%79
        if i==0:
            password1+=lwr_case[t[i]%26]
        if i==k:
            password1+=symbols[t[i]%32]
        if i==j:
            password1+=dgts[t[i]%9]
        password1+=chars[t[i]%79]
    password1+=upr_case[t[i]%26]
    return password1

#to copy password
def copy_to_clipboard(s):
    df=pd.DataFrame([s])
    df.to_clipboard(index=False,header=False)
    label1=tk.Label(text="Password Copied")
    label1.grid(column=1,row=9)
    
#printing password    
def phrase_display():
    greeting=password_generator(var1.get())
    greeting_display=tk.Text(master=window,height=6,width=25)
    greeting_display.grid(column=0,row=4)
    greeting_display.insert(tk.END,greeting)
    button2=tk.Button(text="         COPY         ",command=lambda:copy_to_clipboard(greeting))
    button2.grid(column=1,row=7)

#for display    
label1=tk.Label(text="Welcome to My App")
label1.grid(column=1,row=0)
label2=tk.Label(text="   ")
label2.grid(column=0,row=2)
label2=tk.Label(text="Length of password")
label2.grid(column=0,row=1)

#for selecting length of password
combo = ttk.Combobox(textvariable=var1)
combo['values'] = (12, 13, 14, 15, 16, 
				17, 18, 19, 20, 21, 22, 23, 24, 25, 
				26, 27, 28, 29, 30, 31, 32,) 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(column=1, row=1)

label3=tk.Label(text="Click to Generate Random Passwords\t ")
label3.grid()

#for click button
button1=tk.Button(text="         Click here         ",command=phrase_display)
button1.grid(column=1,row=3)

window.mainloop()
