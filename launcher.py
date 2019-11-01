from tkinter import *
from tkinter import messagebox
import ctypes
import os

kernel32 = ctypes.WinDLL('kernel32') 
user32 = ctypes.WinDLL('user32')
SW_HIDE = 0

hWnd = kernel32.GetConsoleWindow() 
if hWnd: 
    user32.ShowWindow(hWnd, SW_HIDE)

window = Tk()
window.attributes("-fullscreen", True)
window.configure(background='#ADAF9E')

def deleteme(button):
    result = messagebox.askquestion("Confirm", "Are you sure you want to run\n"+button['text']+"\nprogram?", icon='warning')
    if result == 'yes':
        launch(button)

def launch(button):
    if (button['text'] == "Over Estimator\nOut Group"):
        os.startfile("minimumgroupsOO.py")
        window.destroy()
    if (button['text'] == "Over Estimator\nIn Group"):
        os.startfile("minimumgroupsIO.py")
        window.destroy()
    if (button['text'] == "Under Estimator\nOut Group"):
        os.startfile("minimumgroupsIU.py")
        window.destroy()
    if (button['text'] == "Under Estimator\nIn Group"):
        os.startfile("minimumgroupsOU.py")
        window.destroy()
    if (button['text'] == "Control"):
        os.startfile("minimumgroupsC.py")
        window.destroy()

overOut = Button(window, command = lambda: deleteme(overOut), text="Over Estimator\nOut Group", height = 3, width = 15, bg='#80BDA3', font = ('Times New Roman', 45))
overOut.place(x=0, y=0)

overIn = Button(window, command = lambda: deleteme(overIn), text="Over Estimator\nIn Group", height = 3, width = 15, bg='#95CAB6', font = ('Times New Roman', 45))
overIn.place(x=1031, y=0)

underOut = Button(window, command = lambda: deleteme(underOut), text="Under Estimator\nOut Group", height = 3, width = 15, bg='#E3665C', font = ('Times New Roman', 45))
underOut.place(x=0, y=610)

underIn = Button(window, command = lambda: deleteme(underIn), text="Under Estimator\nIn Group", height = 3, width = 15, bg='#C04457', font = ('Times New Roman', 45))
underIn.place(x=1031, y=610)

control = Button(window, command = lambda: deleteme(control), text="Control", height = 3, width = 15, bg='#F7EEA1', font = ('Times New Roman', 45))
control.place(x=515, y=306)

window.mainloop()
