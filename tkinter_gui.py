from tkinter import *
from tkinter import tk


class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.submit = tk.Button(self)
        self.submit["text"] = "Submit"
        self.submit["command"] = self.say_hi
        self.submit.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")
        
        
        mainframe = tk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        
        feet = StringVar()
        meters = StringVar()
        
        feet_entry = tk.Entry(mainframe, width=7, textvariable=feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))
        
        tk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
        tk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
        
        tk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        tk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        tk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
        
        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
        
        feet_entry.focus()
        

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.title("Feet to Meters")
root.bind('<Return>', calculate)

app = Application(master=root)
app.mainloop()





