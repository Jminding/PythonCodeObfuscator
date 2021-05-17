from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import sys
class openFile(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.file = StringVar()
        Button(self, text=" ", command=self.open_file()).grid(row=2, column=0, sticky=W)
        Button(self, text="Obfuscate", command=self.obfuscate).grid(row=3, column=0, sticky=W)
    def open_file(self):
        self.name = filedialog.askopenfilename()
        Label(self, text=self.name).grid(row=0, column=0, sticky=W)
    def obfuscate(self):
        code = open(self.name)
        new = code.read()
        new_2 = "\\n".join(new.split("\n"))
        code = open(self.name, "w")
        code.write(f'exec("""{new_2}""")')
        messagebox.showinfo(title=None, message="I have finished obfuscating your code!")
        sys.exit()
root = Tk()
root.title("Python Code Obfuscator")
file = openFile(root)
file.mainloop()
