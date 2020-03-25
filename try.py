from tkinter import *
import matplotlib
from tkinter.filedialog import askopenfilename
import tkinter as tk 

class Window(Frame):



    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("AnalPy")

        self.pack(fill=BOTH, expand=1)

        entry_label = tk.Label(root, text = "Import any file.")
        entry_label.pack()

        menu = Menu(self.master)

        self.master.config(menu=menu)
        #Code for drop-down options
        file = Menu(menu)

        file.add_command(label="Import CSV", command=self.import_csv)

        file.add_command(label="Exit", command=self.client_exit)

        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)

        edit.add_command(label="Undo")

        menu.add_cascade(label="edit", menu=edit)

    

    def client_exit(self):
        exit()

    
    def import_csv(self):

        filepath = askopenfilename()
        print(filepath)




root = Tk()

root.geometry("600x800")

app = Window(root)

# entry_label = tk.Label(root, text = "Import any file.")
# entry_label.pack()

root.mainloop()
