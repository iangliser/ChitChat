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
participantID = input("Enter Participant ID: ")

file1 = open("ParticipantNumber.txt", "w")
file2 = open("./scriptReader/ParticipantNumber.txt", "w")
file3 = open("./TypeTask/ParticipantNumber.txt", "w")
file1.write(participantID)
file2.write(participantID)
file3.write(participantID)
file1.close()
file2.close()
file3.close()
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
checker = 0
skip = 0

procCount = 0
procArrayCount = 1
procList = []

outroCount = 0
answer = []

# LABEL WIDGET
startImage = tkobj.PhotoImage(file=".\\sample_images\\proc\\proc.png")
enterImage = tkobj.PhotoImage(file=".\\sample_images\\enterImage.png")

# underEstimateStartImage = tkobj.PhotoImage(file=".\\sample_images\\underEstimator\\underEstimator.png")
# underEstimatePatchImage = tkobj.PhotoImage(file=".\\sample_images\\underEstimator\\underEstimatorPatch.png")
wait = tkobj.PhotoImage(file=".\\sample_images\\waitScreen.png")
notify = tkobj.PhotoImage(file= ".\\sample_images\\notify.png")
patchImg = tkobj.PhotoImage(file= ".\\sample_images\\patch.png")
underEstimateImage1 = tkobj.PhotoImage(file=".\\sample_images\\underEstimator\\underEstimator1.png")
underEstimateImage2 = tkobj.PhotoImage(file=".\\sample_images\\underEstimator\\underEstimator2.png")
underEstimateImage3 = tkobj.PhotoImage(file=".\\sample_images\\underEstimator\\underEstimator3.png")

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
while procArrayCount < 8:  # Amount of Images is n - 1 = 6
    procList.append(tkobj.PhotoImage(file=".\\sample_images\\proc\\proc" + str(procArrayCount) + ".png"))
    procArrayCount += 1
#####CHNG NMR
# Creates array of point images for procedure
while count < 41:  # Amount of Images is n - 1 = 40
    pointList.append(tkobj.PhotoImage(file=".\\sample_images\\points\\point (" + str(count) + ").png"))
    count += 1

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
    if procCount > 7:
        checkpoint = 1
    elif procCount == 7:  # Condiiton to force participant to press enter twice
        procCount += 1
    else:
        label.configure(image=procList[procCount])
        procCount += 1

###CHNG DOT NUMBER
def nextImg(press):  # Checkpoint 1
    global nextCount, label, checkpoint, skip
    if nextCount == 40:
        checkpoint = 2
    else:
        if(skip == 0):
            skip = 1
            txt.delete(0, 'end')
            txt.configure(state='disabled')
            label.configure(image=pointList[nextCount])
            nextCount += 1
            window.after(1000, next, keyboard.is_pressed('enter'))
        else:
            if(len(txt.get()) < 1):
                next('<Return>')
            else:
                txt.delete(0, 'end')
                txt.configure(state='disabled')
                label.configure(image=pointList[nextCount])
                nextCount = nextCount + 1
                window.after(1000, next, keyboard.is_pressed('enter'))

def next(press):
    global answer, nextCount, checker
    txt.pack(ipady=5, pady=100)
    txt.configure(state='normal')
    label.configure(image=enterImage)


def loadScrn():
    global outroCount, checkpoint
    if outroCount == 7:
        label.configure(image=underEstimateImage1)
    elif outroCount == 8:
        label.configure(image=underEstimateImage2)
    elif outroCount == 9:
        label.configure(image=underEstimateImage3)
    else:
        checkpoint = 3


def placement(press):  # Checkpoint 2
    global checkpoint, outroCount, label
    if outroCount == 0:
        label.configure(image=notify)
        outroCount += 1
    elif outroCount == 1:
        label.configure(image=rules1)
        # window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount += 1
    elif outroCount == 2:
        label.configure(image=rules2)
        # window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount += 1
    elif outroCount == 3:
        txt.configure(state='disabled')
        label.configure(image=rules3)
        # window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount += 1
    elif outroCount == 4:
        label.configure(image=rules4)
        # window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount += 1
    elif outroCount == 5:
        label.configure(image=rules5)
        window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount += 1
    elif outroCount == 6:
        window.bind('<Return>', disable)
        label.configure(image=wait)
        #window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount += 1
    elif outroCount == 7:
        window.bind('<Return>', pressed)
        window.after(5000, loadScrn())
        outroCount += 1
    elif outroCount == 8:
        window.bind('<Return>', disable)
        label.configure(image=underEstimateImage2)
        window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount += 1
    elif outroCount == 9:
        window.bind('<Return>', pressed)
        window.after(5000, loadScrn())
        outroCount += 1
    elif outroCount == 10:
        label.configure(image=patchImg)
        window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount += 1
    elif outroCount == 11:
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
        'https://unh.az1.qualtrics.com/jfe/form/SV_9uAwu18LcWS3ioR')


def keylogger():
    os.system('keylogFINAL.py')


window.bind('<Return>', pressed)

window.mainloop()