#Daniel Berkowitz - pytypeseed
import csv
from threading import Timer
from time import time
import signal
from pip._vendor.distlib.compat import raw_input

i = 0
timeout=10
t=Timer(timeout,print,"hello")
cs = False
prompt = "A lot of things remind me of my father who passed away when I was 24. Driving on certain back roads he showed me. Stopping at certain stores he always used to go to. Eating at his favorite places. More and more of these places are fading away too though. The roads keep getting built up more and more. The shops and restaurants are closing down."  ##At first it was heart breaking that my father wasn't in this world anymore. But slowly the things that remind me of him are leaving this world as well.A lot of things remind me of my father who passed away when I was 24. Driving on certain back roads he showed me. Stopping at certain stores he always used to go to. Eating at his favorite places. More and more of these places are fading away too though. The roads keep getting built up more and more. The shops and restaurants are closing down. At first it was heart breaking that my father wasn't in this world anymore. But slowly the things that remind me of him are leaving this world as well."

participantNum = input("Enter Participant Number: ")
namer = "./Participant" + participantNum + "_typedata.csv"


def counter():
    i = 0
    print (prompt)
    raw_input(">> Press ENTER to begin")
    begin_time = time()
    #t.start()
    signal.alarm(10)
    inp = raw_input("\n")
    t.cancel()
    return  inp


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








