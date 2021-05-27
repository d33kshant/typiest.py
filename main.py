import sys, time, random
from difflib import SequenceMatcher

def printTarget(text):
    print(f'\n\033[1;34;40m{text}\033[0;0m')

def printStats(w, t, wpm, acc):
    print(f'\n\033[0;32;40mStats\n\033[0;0mTotal Words: {w}\nTime Taken: {round(t,4)}sec\nWords/Minute: {wpm}\nAccurecy: {acc}')

def check(phrase, typed):
    pass

def start():
    wpm = 0
    acc = 0
    words = 0
    types = []
    targets = []
    takenTimes = []
    phrases = open('phrases.txt').read().split('\n')
    while len(phrases) != 0:
        #Get random index
        rIndex = random.randint(0, len(phrases)-1)
        
        #Print phrase at that index and take input from user
        printTarget(phrases[rIndex])
        tStart = time.time()
        inp = input(":")
        correctWords = check(phrases[rIndex], inp)
        tTaken = time.time() - tStart
        if(inp == ''):
            break
        takenTimes.append(tTaken)

        #Add 
        types.append(inp)
        words += len(inp.split(" "))
        targets.append(phrases[rIndex])
        phrases.pop(rIndex)
    totalTime = sum(takenTimes)
    accs = []
    for i in range(len(types)):
        a = SequenceMatcher(None, types[i], targets[i]).ratio()
        accs.append(a)
    acc = (sum(accs)/len(accs))*100
    if totalTime != 0:
        wpm = int((words/totalTime)*60)
    printStats(words, totalTime, wpm, round(acc, 4))

def printHelp():
    print("\033[1;34;40mTypiest:\033[0;0m A console based typing speed test.\n")
    print("\033[0;32;40mUsage:\033[0;0m")
    print("Just run the program with 'start' argument")
    print("A random phrase of 6 word will apear")
    print("Type it as fast and accurate you can\n")
    print("\033[0;33;40mNote:\033[0;0m")
    print("To exit program press return key instaed of typing phrase")
    print("By default 100 phrases will be tested")

if __name__ == '__main__':
    argc = len(sys.argv)
    args = sys.argv
    if argc != 2:
        print("\033[0;31;40mInvalid Arguments. Use 'main.py help' for details.\033[0;0m")
    else:
        if args[1] == 'help':
            printHelp()
        elif args[1] == 'start':
            start()
        else:
            print("\033[0;31;40mInvalid Arguments. Use help for details.\033[0;0m")