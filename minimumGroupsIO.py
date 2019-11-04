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
submit = tkobj.PhotoImage(file=".\\sample_images\\submit.png")
notify = tkobj.PhotoImage(file= ".\\sample_images\\notify.png")
patchImg = tkobj.PhotoImage(file= ".\\sample_images\\patch.png")
overEstimateImage1 = tkobj.PhotoImage(file=".\\sample_images\\overEstimator\\overEstimator1.png")
overEstimateImage2 = tkobj.PhotoImage(file=".\\sample_images\\overEstimator\\overEstimator2.png")
overEstimateImage3 = tkobj.PhotoImage(file=".\\sample_images\\overEstimator\\overEstimator3.png")

rules1 = tkobj.PhotoImage(file=".\\sample_images\\rules\\rules1.png")
rules2 = tkobj.PhotoImage(file=".\\sample_images\\rules\\rules2.png")
rules2dot5= tkobj.PhotoImage(file=".\\sample_images\\rules\\rules2_5.png")
rules3 = tkobj.PhotoImage(file=".\\sample_images\\rules\\rules3.png")
rules4 = tkobj.PhotoImage(file=".\\sample_images\\rules\\rules4.png")
rules5 = tkobj.PhotoImage(file=".\\sample_images\\rules\\rules5.png")
rules6 = tkobj.PhotoImage(file=".\\sample_images\\rules\\rules6.png")
rules7 = tkobj.PhotoImage(file=".\\sample_images\\rules\\rules7.png")
rules8 = tkobj.PhotoImage(file=".\\sample_images\\rules\\rules8.png")
rules9 = tkobj.PhotoImage(file=".\\sample_images\\rules\\rules9.png")
rules10 = tkobj.PhotoImage(file=".\\sample_images\\rules\\rules10.png")
rules11 = tkobj.PhotoImage(file=".\\sample_images\\rules\\rules11.png")
rules12 = tkobj.PhotoImage(file=".\\sample_images\\rules\\rules12.png")
rules13 = tkobj.PhotoImage(file=".\\sample_images\\rules\\rules13.png")
rules14 = tkobj.PhotoImage(file=".\\sample_images\\rules\\rules14.png")
chatserv = tkobj.PhotoImage(file=".\\sample_images\\rules\\chatserv.png")


# PROCEDURE IMGS !!!
"""
proc1 = tkobj.PhotoImage(file=".\\sample_images\\proc1.png")
proc2 = tkobj.PhotoImage(file=".\\sample_images\\proc2.png")
"""

label = tkobj.Label(image=startImage)
label.pack(expand=1)

# Creates array of start images for introduction before procedure
while procArrayCount < 11:  # Amount of Images is n - 1 = 6
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
    if procCount > 10:
        checkpoint = 1
    elif procCount == 10:  # Condiiton to force participant to press enter twice
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
            window.bind('<Return>',disable)
            nextCount += 1
            window.after(1000, next, keyboard.is_pressed('enter'))
        else:
            if(len(txt.get()) < 1):
                next('<Return>')
            else:
                txt.delete(0, 'end')
                txt.configure(state='disabled')
                label.configure(image=pointList[nextCount])
                window.bind('<Return>',disable)
                nextCount = nextCount + 1
                window.after(1000, next, keyboard.is_pressed('enter'))

def next(press):
    global answer, nextCount, checker
    window.bind('<Return>', pressed)
    txt.pack(ipady=5, pady=100)
    txt.configure(state='normal')
    label.configure(image=enterImage)

def loadScrn():
    global outroCount, checkpoint
    if outroCount == 18:
        label.configure(image=overEstimateImage1)
        #outroCount +=1
    elif outroCount == 19:
        label.configure(image=overEstimateImage2)
        #outroCount += 1
    elif outroCount == 20:
        label.configure(image=overEstimateImage3)
        #outroCount += 1
    elif outroCount == 22:
        checkpoint = 3

def placement(press):  # Checkpoint 2
    global checkpoint, outroCount, label
    if outroCount == 0:
        label.configure(image=submit)
        outroCount += 1
    elif outroCount == 1:
        label.configure(image=notify)
        # window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount += 1
    elif outroCount == 2:
        label.configure(image=rules1)
        #window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount+=1
    elif outroCount == 3:
        label.configure(image=rules2)
        #window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount += 1
    elif outroCount ==4:
        label.configure(image=rules2dot5)
        outroCount+=1
    elif outroCount == 5:
        label.configure(image=rules3)
        outroCount += 1
    elif outroCount ==6:
        label.configure(image=rules4)
        outroCount+=1
    elif outroCount ==7:
        label.configure(image=rules5)
        outroCount+=1
    elif outroCount ==8:
        label.configure(image=rules6)
        outroCount+=1
    elif outroCount ==9:
        label.configure(image=rules7)
        outroCount+=1
    elif outroCount ==10:
        label.configure(image=rules8)
        outroCount+=1
    elif outroCount ==11:
        label.configure(image=rules9)
        outroCount+=1
    elif outroCount ==12:
        label.configure(image=rules10)
        outroCount+=1
    elif outroCount ==13:
        label.configure(image=rules11)
        outroCount+=1
    elif outroCount ==14:
        label.configure(image=rules12)
        outroCount+=1
    elif outroCount ==15:
        label.configure(image=rules13)
        outroCount+=1
    elif outroCount ==16:
        label.configure(image=rules14)
        outroCount+=1
    elif outroCount == 17:
        window.bind('<Return>', disable)
        label.configure(image=wait)
        window.after(5000, placement, keyboard.is_pressed('enter'))
        outroCount +=1
    elif outroCount == 18:
        window.after(5000, loadScrn())
        window.bind('<Return>', pressed)
        outroCount += 1
    elif outroCount == 19:
        window.bind('<Return>', disable)
        label.configure(image=overEstimateImage2)
        window.after(5000,placement, keyboard.is_pressed('enter'))
        outroCount += 1
    elif outroCount == 20:
        window.bind('<Return>', pressed)
        window.after(5000, loadScrn())
        outroCount += 1
    elif outroCount == 21:
        label.configure(image=chatserv)
        outroCount +=1
    else: checkpoint = 3

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