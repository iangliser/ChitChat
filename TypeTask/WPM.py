#Daniel Berkowitz - pytypeseed
import csv

from time import time

from pip._vendor.distlib.compat import raw_input

i = 0
cs = False
prompt = "There are many idiosyncratic typing styles in between novice-style 'hunt and peck' and touch typing. For example, many hunt and peck typists have the keyboard layout memorized and are able to type while focusing their gaze on the screen. Some use just two fingers, while others use 3-6 fingers. Some use their fingers very consistently, with the same finger being used to type the same character every time, while others  vary the way they use their fingers."


file = open("ParticipantNumber.txt", "r")
participantNum = file.read()
namer = "./typeData/Participant" + participantNum + "_typedata.csv"

def counter():
    i = 0
    raw_input(">> Press ENTER to begin. \n Once you finish typing out the statement, press ENTER again to record your results. \n \n")
    print (prompt)
    begin_time = time()
    inp = raw_input("\n")
    end_time = time()
    final_time = (end_time - begin_time) / 60
    return final_time, inp


def wpm(time, line):
    words = line.split()
    word_length = len(words)
    words_per_m = word_length / time
    return words_per_m


def wordcheck(inp):
    prompts = prompt.split()
    inputs = inp.split()
    errorcount = 0

    idx = 0
    for inp in inputs:
        if inp != prompts[idx]:
            errorcount += 1
            if inp == prompts[idx + 1]:
                idx += 2
            elif inp != prompts[idx - 1]:
                idx += 1
        else:
            idx += 1

    words_left = len(prompts) - len(inputs)
    correct = float(len(prompts)) - float(errorcount)
    percentage = (((float(correct) / float(len(prompts))) - float(words_left) / float(len(prompts))) * 100)

    return percentage

tm, line = counter()
tm = round(tm, 2)
words_per_minute = wpm(tm, line)
words_per_minute = round(words_per_minute, 2)
percentage = wordcheck(line)
percentager = round(percentage, 2)

f = open(namer, "w+")
writer = csv.writer(f)
f.write("Time elapsed" + "," + str(tm))
writer.writerow(" ")
f.write("WPM" + "," + str(words_per_minute))
writer.writerow(" ")
f.write("Accuracy" + "," + str(percentager))
f.close()


print("Your total time was:" + str(tm) + " minutes")
print("with an average of:" +str (words_per_minute) +  "words per minute") #% words_per_minute
print("with an accuracy of:" +  str(percentager) +"%") #% percentager



