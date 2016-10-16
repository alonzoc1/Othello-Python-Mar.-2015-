import tkinter

master = tkinter.Tk()

variable = tkinter.StringVar(master)
variable.set("one") # default value

w = tkinter.OptionMenu(master, variable, "one", "two", "three")
z = tkinter.OptionMenu(master, variable, "not", "even","close")
w.pack()
z.pack()

tkinter.mainloop()
