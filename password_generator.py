import random
import tkinter as tk
import string
import pandas as pd
window=tk.Tk()
window.geometry("600x300")
window.title("**ViSpY**")

def password_generator():
    normal = string.ascii_uppercase + string.ascii_lowercase + string.digits
    symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
    chars= normal + symbols
    password1 = ''
    password1+=random.choice(string.ascii_lowercase)
    name=random.randrange(12,32)
    j=int(name/2)
    for i in range(name-3):
        if i==j:
            password1+=random.choice(string.digits)
        password1+=random.choice(chars)
    password1+=random.choice(string.ascii_uppercase)
    return password1

def copy_to_clipboard(s):
    df=pd.DataFrame([s])
    df.to_clipboard(index=False,header=False)
    label1=tk.Label(text="Password is copied to clipboard")
    label1.grid(column=1,row=9)
    
    
def phrase_display():
    greeting=password_generator()
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
label3=tk.Label(text="Click to Generate Random Passwords\t ")
label3.grid()

#for click button
button1=tk.Button(text="         Click here         ",command=phrase_display)
button1.grid(column=1,row=3)
window.mainloop()
