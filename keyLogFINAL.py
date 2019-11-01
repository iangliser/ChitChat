import pynput
import csv
import datetime
import ctypes  # used for hiding shell
from pynput.keyboard import Key, Listener
import winsound
import pyglet

writeCount = 0

keys = []  # Array which holds keys pressed
times = []  # Array which holds the times of key pressed, times[x] refers to the key of key[x]

mwbutton=pyglet.resource.media('mwbutton_short.wav')

kernel32 = ctypes.WinDLL('kernel32')  # Declaration of variables which will be used later to hide shell, ctypes library
user32 = ctypes.WinDLL('user32')
SW_HIDE = 0

#participantNum = input("Enter Participant Number: ")

hWnd = kernel32.GetConsoleWindow()  # Returns boolean based upon if the shell is shown or not
if hWnd:  # If the shell is visible then hide
    user32.ShowWindow(hWnd, SW_HIDE)
    # formats a dateTime output for fileName
    # Year-Month-Day_Hour.Minute (had to use this format because filename restrictions)
    # concatenates the dateTime formatter into a .csv

file = open("ParticipantNumber.txt","r")
participantID = file.read()

namer = "./keydata/Participant" + str(participantID) +  str(datetime.datetime.now().strftime("_%Y-%m-%d_%H.%M")) + ".csv"

#insert #minimumGroups.participantID# into namer var

def on_press(key):
    global keys, times
    keys.append(key)  # Add the key pressed to keys[] array
    pressTime = (datetime.datetime.utcnow())  # Get current time
    if key == Key.ctrl_l:
      winsound.PlaySound('mwbutton_short.wav',winsound.SND_FILENAME) #plays sound when Mind Wandering button is pressed
    times.append(
        pressTime)  # add time to time[] array, script breaks if you do not use a variable proxy such as 'presstime'
    print(str("{0}".format(key)) + "," + str(
        pressTime))  # print to shell the key and time, could be removed as the shell is hidden
    write_file(keys)  # call the file writing method


def write_file(keys):
    with open(namer, "w") as f:  # create csv with filename of 'namer', 'w' indicates that we are writing a csv
        writer = csv.writer(f)
        count = 0
        f.write("Participant ID," + participantID + "\n")
        while count < len(keys):  # loop will cycle through whole array of keys
            if str(keys[count]) == "','":
                f.write("\",\"" + "," + str(times[count]) + "\t")
            else:
                f.write(str(keys[count]) + "," + str(times[count]) + "\t" + "\n")  # write a row of csv

            #writer.writerow(" ")  # write a return (results in newline in csv)
            count += 1


def on_release(key):  # end program if 'esc' is pressed
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:  # main runner of program, of the csv library
    listener.join()