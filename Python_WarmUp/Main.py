import ChatBot as cb
import glob as g

def manual():
    
    print("Hello are you female or male? (male/female)")
    inputStr = input()
    inputStr = cb.processInput()
    cb.chat1response(inputStr)
    
    print

    defaultResponse = inputStr[-1] + " awesome, but I hate " + inputStr[0] +  " too. Bye for now."

def automatic():
    dirList = g.glob("C:\Users\Joshua Salas\Desktop\CS4375\Python_WarmUp\chatTest\*.txt")  #This dir will change based on the system
    print("Select a file to run (type a number from the list) \n" + enumerate(dirList))
    fileNumber = input()

    # Getting file as list
    with open(dirList[fileNumber]) as fileChoice:
        lines = [line.strip().split(',') for line in fileChoice]

    i = 0
    print("Hello are you female or male? (male/female)")
    if(lines[i] in cb.chat1Responses):
        print(cb.chat1Responses[lines[i]])
        i += 1
        if(lines[i] in cb.chat2Responses):
            print(cb.chat2Responses[lines[i]])
    print(cb.defaultResponse)
        


def modeSelector():
    print("Would you like automatic or manual mode?")
    mode = input()

if __name__=='__main__':
    modeSelector()