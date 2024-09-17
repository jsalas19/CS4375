
inputStr = ""

chat1Responses = {"female": "How excellent! Are you a CS major? (yes/no)", "male":"Me too. Are you a CS major? (yes/no)"}
chat2Responses = {"yes": "Excellent, I am too. What's an animal you don't like, and two you do?",
                 "no":  "Too bad. Anyway, what's an animal you like, and you don't?"}

errorMessage = "Please input a valid reponse"

defaultResponse = inputStr[-1] + " awesome, but I hate " + inputStr[0] +  " too. Bye for now."


'''
response() processes the user input and will determine the appropriate output for any given user
input. 
'''
def chat1response(iS):
    if(iS in chat1Responses): return chat1Responses[iS]
    return 
        

def processInput():
    
    inputStr = inputStr.split(" ")
    inputStr = inputStr.lower()
