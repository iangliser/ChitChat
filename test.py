import tkinter as tkobj
from itertools import cycle

window = tkobj.Tk()

#WINDOW PROPERTIES
window.title("Minimum Groups")
window.attributes("-fullscreen", True)

dotsList=[]
count = 1
nextCount = 1

while count<11:
	dotsList.append(tkobj.PhotoImage(file=".\\sample_images\\dots (" + str(count) + ").png"))
	count = count + 1

#LABEL WIDGET
#image0 = tkobj.PhotoImage(file=".\\sample_images\\dots1.png")
label = tkobj.Label(tkobj.PhotoImage(file="\\sample_images\\start.png"))
label.pack(expand=True)

#ENTRY WIDGET 
fontType= ('Times New Roman', 30)
txt = tkobj.Entry(window,font=fontType,width=5,justify="center")
txt.focus()
txt.pack(ipady=5, pady=100)

def nextImg(press):
	global nextCount
	label.configure(image=dotsList[nextCount])
	nextCount = nextCount + 1

window.bind('<Return>', nextImg)

window.mainloop()