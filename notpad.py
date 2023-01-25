from tkinter import *
from tkinter import messagebox,font
from datetime import datetime
from tkinter import filedialog
# from tkinter.scrolledtext import ScrolledText
import webbrowser

t=Tk()
t.title("Notpad")
t.geometry("800x500")

# def fun():
#     print('im Function')
def save():
        pass

def exit():
        message = messagebox.askquestion('Notepad',"Do you want to save changes")
        if message == "yes":
            save()
        else:
            t.destroy()

mymenu=Menu(t)
t.config(menu=mymenu)

submenu=Menu(mymenu)
mymenu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New")
submenu.add_command(label="New window")
submenu.add_command(label="Open")
submenu.add_command(label="Save",command=save)
submenu.add_command(label="Save As...")
submenu.add_separator()
submenu.add_command(label="Page Setup")
submenu.add_command(label="Print..")
submenu.add_separator()
submenu.add_command(label="Exit",command=exit ,background="red" ,font=('ariel',10,'italic'))

# Editmenu
edit=Menu(mymenu)
mymenu.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Undo")
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_separator()
edit.add_command(label="Search with bing...")
edit.add_command(label="Find")
edit.add_command(label="Find Next")
edit.add_command(label="Find Previous")
edit.add_command(label="Replace")
edit.add_command(label="Go To..")
edit.add_command(label="Select All")
edit.add_command(label="Time /Date")
edit.add_separator()

# Format

formati=Menu(mymenu)
mymenu.add_cascade(label="Format",menu=formati)
formati.add_command(label="Word Wrap")
formati.add_command(label="Font...")


# View
view=Menu(mymenu)
mymenu.add_cascade(label="View",menu=view)
view.add_command(label="Zoom")
view.add_command(label="Status Bar")

# Help
def view_help():
    webbrowser.open('#')

helpi=Menu(mymenu)
mymenu.add_cascade(label="Help",menu=helpi)
helpi.add_command(label="View help",command=view_help)
helpi.add_command(label="Send feedback",command=view_help)
helpi.add_separator()
helpi.add_command(label="About notpad..",command=view_help)



t.mainloop()