
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

    match inputStr:
        case "female":
            return "How excellent! Are you a CS major?"
        case "male":
            return "Me too. Are you a CS major?"
        case "yes":
            return "Excellent, I am too. What's an animal you don't like, and two you do?"
        case "no":
            return "Too bad. Anyway, what's an animal you like, and you don't?"
        case _:
            return  inputStr[-1] + " awesome, but I hate " + inputStr[0] +  " too. Bye for now."
        

def processInput():
    
    inputStr = inputStr.split(" ")
    inputStr = inputStr.lower()
