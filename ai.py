import random

print("=====Test=====")

# Sentences we'll respond with if the user greeted us
greetingWords= ("hello", "hi", "greetings", "sup", "what's up","hello bot", "hi,")
greetingResposes = ["Sup bro", "Hey", "*nods*","Hello"]


"""
Checks if the person greeted the Bot
"""
def checkForGreeting(yourResponse):
    for word in yourResponse.split():#read words not letters
        if word.lower() in greetingWords:
            return random.choice(greetingResposes)


#"""

#"""
        

def chat():
    yourResponse = None
    while (True):
        yourResponse = input("\nYou: ")
        
        botResponse = checkForGreeting(yourResponse)
        
        if checkForGreeting(yourResponse) == None:
            print("Bot: No hello ouch")
        else:
            print("Bot:",end="")
            for char in botResponse:
                print(char,end="")

chat()


