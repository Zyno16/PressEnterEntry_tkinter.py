from tkinter import *
from tkinter import ttk
from tools import *
form =Tk()
form.geometry("700x500")



def test():
    msgbox("test")
txt=ttk.Entry(form)
txt.pack()
ttk.Button(form,text="okay").pack()

txt.bind("<Return>",lambda my:test())
fontall(form,"None 25")


form.mainloop()
