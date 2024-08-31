
inputStr = ""

initialResponse = "Hello are you female or male?"
chatResponses = {"female": "How excellent! Are you a CS major?", "male":"Me too. Are you a CS major?",
                 "yes": "Excellent, I am too. What's an animal you don't like, and two you do?",
                 "no":  "Too bad. Anyway, what's an animal you like, and you don't?"}
defaultResponse = inputStr[-1] + " awesome, but I hate " + inputStr[0] +  " too. Bye for now."


'''
response() processes the user input and will determine the appropriate output for any given user
input. 
'''
def response(iS):
    inputStr = iS

    processInput()

        

def processInput():
    
    inputStr = inputStr.split(" ")
    inputStr = inputStr.lower()
