
from tkinter import *
from tkinter import ttk
top=Tk()
top.maxsize(width=400,height=400)
top.minsize(width=400,height=400)
def fn():
    pass
my_menu=Menu(top)
top.config(menu=my_menu)

file_menu=Menu(my_menu)
my_menu.add_cascade(label="file",menu=file_menu)
file_menu.add_cascade(label="new",command=fn)
file_menu.add_cascade(label="open",command=fn)

edit_menu=Menu(my_menu)
my_menu.add_cascade(label="edit",menu=edit_menu)
edit_menu.add_cascade(label="undo",command=fn)
edit_menu.add_cascade(label="delete",command=fn)
edit_menu.add_separator()
edit_menu.add_cascade(label="install new software",command=fn)
top.mainloop()