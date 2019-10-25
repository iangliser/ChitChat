from tkinter import *
import csv
import ctypes

#Declaration of variables which will be used later to hide shell, ctypes library
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_HIDE = 0

#Input variables: pNum for csv output name, file name for reading the ChatPlat csv
participantNum = input("Enter Participant Number: ")
fileName = "./" + input("Enter name of the script/CSV: ")  + ".csv"

hWnd = kernel32.GetConsoleWindow() #Returns boolean based upon if the shell is shown or not
if hWnd: #If the shell is visible then hide
    user32.ShowWindow(hWnd, SW_HIDE)

#Basic tkinter window creation & attributes of window
window = Tk()
window.attributes("-fullscreen", True)

#variable declarations
namer = "topicShift" + str(participantNum) + ".csv"
count = 0
counter = 0
data = 0
dataStore = []

#Creation of text widget, this is the main widget in which all others are added into
T = Text(window, height=20, width=80, font = ('Times New Roman', 30), state='disabled')#default is disabled so the user cannot type or delete text
T.pack() #.pack() is responsible for displaying the widget, pack is used instead of other options (ie place/geometry) because
		 #the text widget remains in full screen

#File write function that is called by finishButton
def write_file():
	with open(namer, "w") as scriptWrite: #open (if not existing then create) the file with purpose of writing denoted by "w"
		with open(fileName) as csvFile: #open ChatPlat csv in order to get messages and usernames
			global counter
			scriptTwo = csv.DictReader(csvFile) #dictReader objects let us read from specific rows by header
			writer = csv.writer(scriptWrite)
			preRows = []
			preDataStore = []
			preUsers = []
			for item in dataStore: preDataStore.append(item.get()) #fill individual lists with elements in preperation to zip
			for row in scriptTwo:
				preRows.append(row["Message"])
				preUsers.append(row["User"])
			rows = zip(preDataStore, preUsers, preRows) #zip lists combines lists as in this example: [1,2] [a,b] [x,y] ==> [(1,a,x), (2,b,y)]
			for row in rows: #For each row there is in the new lists write the elements
				writer.writerow(row)
			window.quit() #finally close the program

#This portion is responsible for the create of all checkbuttons
with open(fileName) as csvFile:
	script = csv.DictReader(csvFile) #creation of dictreader objects for easy iteration through specific rows
	scriptTwo = csv.DictReader(csvFile)
	T.configure(state='normal') 	#here we add a newline inbetween buttons, normal state allows the text widget to be edited
	T.insert("end", "\n")       	#and because we would not like the user to edit text it must be set to normal, then edited
	T.configure(state='disabled')	#then set back to disabled
	for row in script:
		dataStore.append(IntVar(value=0))#Creates an array of tkinter IntVar's of 0 that are then set as the checkbuttons variable
		cb = Checkbutton(window, text=row["User"] + ": " + row["Message"], variable = dataStore[count], font = ('Times New Roman', 16), bg = 'white')
		T.window_create("end", window=cb) #window_create places the checkbutton inside of the text widget
		T.configure(state='normal')
		T.insert("end", "\n")
		T.configure(state='disabled')
		count += 1

#Button placed at the top of the program that executes write_file()
#The 'text=...' portion is sloppy because aligning the button in a text widget while using .pack() for the text widget proved to be quite challenging
#As for now this will do..
finishButton = Button(window, text="Finish", command = write_file, font = ('Times New Roman', 18))
T.window_create("end", window=finishButton, align = 'baseline')

window.mainloop()
