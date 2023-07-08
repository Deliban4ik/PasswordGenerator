import tkinter as tk
from tkinter import Tk
from password import create_password

root=Tk()
root["bg"]="#303030"
root.geometry("300x70")
root.title("Generator by Deliban4ik")

def pas():
    length=int(entry.get())
    password=create_password(length)
    label["bg"]="#808080"
    label["text"]=password
    label.update()
    with open("passwords.txt", "a") as file:
        file.write(f"length={length}, password={password};\n")
        file.close()
    


button = tk.Button(background="#808080",
text="Click me to create a password", 
command=pas)
button.place(x=70,y=45)
entry=tk.Entry(background="#808080")
entry.place(x=7,y=45, width=30, height=25)
label=tk.Label(bg="#303030")
label.place(x=70,y=10)
root.mainloop()