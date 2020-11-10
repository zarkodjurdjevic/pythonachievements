
isRunning = True
boodschappen = []

def additem(givenList):

    print("wat wil je toevoegen")
    antwoord = input()
    givenList.append(antwoord)


def removeitem(givenList):

    print("dit zit er in je lijst")
    print(givenList)
    print("welk wil je uit je lijst")

    antwoord = input()
    #givenList.remove(antwoord)
    for item in givenList:
        if (item == antwoord):
            givenList.remove(item)


def update():

    global isRunning, boodschappen
    
    

    
    print("wil je iets toevoegen [add] of verwijderen [remove] aan je lijst")
    tekst = input()


    if (tekst == "add"):
          #boodschappen.append(tekst)
          additem(boodschappen)

    elif (tekst == "remove"):
          removeitem(boodschappen)

    elif (tekst == "exit"):
          print("sluit af")  
          isRunning = False
    else:
        print("tekst is wat anders:", tekst)
    
    print(boodschappen)


while isRunning == True:

    update()

    
