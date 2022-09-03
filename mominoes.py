from tkinter import*
from PIL import imageTk, image
from ykinter import ttk
root = Tk()
root.geometry("900x899")

burger = ImageTk,PhotoImage(image.open("burger"))
burger_image=label(root)
burger_image["image"]=burger
burger_image.place(relx=0.12, rely=0.5, anchor=CENTER)


label_heading=label(root,text="mominos",font=("times",40,"bolder"),fg="Orange")
label_heading.place(relx=0.13,rely=0.1,anchor=CENTER)



label_select_dish=label(root,text="select dish",font=("times",40))
label_heading.place(relx=0.13,rely=0.1,anchor=CENTER)

dishlist=["pizza","cold_coffee"]
label_dropdown=ttk.Combobox(root,state="readonly",value= dishlist)
label_heading.place(relx=0.25,rely=0.2,anchor=CENTER)