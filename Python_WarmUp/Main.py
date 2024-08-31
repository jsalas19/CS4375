import ChatBot as cb

'''
chat1Responses = {"female": "How excellent! Are you a CS major?", "male":"Me too. Are you a CS major?"}
chat2Responses = {"yes": "Excellent, I am too. What's an animal you don't like, and two you do?",
                 "no":  "Too bad. Anyway, what's an animal you like, and you don't?"}
'''
def main():
    
    print("Hello are you female or male?")
    inputStr = input()
    inputStr = cb.processInput()
    chat1Responses(inputStr)
    
    print

    defaultResponse = inputStr[-1] + " awesome, but I hate " + inputStr[0] +  " too. Bye for now."



if __name__=='__main__':
    main()