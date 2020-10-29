print("kies uit de onderstaande keuzes welke keuzes jij zou nemen op en schooldag.")
print("je word wakker op een vroege maandag ochtend je ziet dat je genoeg tijd hebt")
print("voordat je naar school moet gaan.")
print("#########################################################################")
print("je bent net uit de douch gestapt en je moet nog eten. kies uit A,B of C wat je wilt eten")
print("A = boterham met kaas")
print("B = cruesli")
print("C = pannenkoeken")
antwoord = input()
if antwoord.upper() == "A":
    print("je hebt heerlijk genoten van je boterham")
elif antwoord == "B" or antwoord == "b":
    print("je hebt heerlijk genoten van je ontbijt")
else:
    print("de pannenkoeken hebben je goed gedaan je voelt je gelijk lekker in je vel")
print("na heerlijk ontbijt te hebben in je badjas moet je, je omkleden kies wat je aan wilt doen.")
print("A = trainingspak")
print("B = Polo met spijkerbroek")
print("C = blouse met spijkerbroek")
antwoord = input()
if antwoord == "A" or antwoord == "a":
    print("je hebt je mooiste trainingspak aangetrokken")
elif antwoord == "B" or antwoord == "b":
    print("je hebt een leuke polo met en spijkerbroek aangedaan")
else:
    print("je hebt een leuke blouse met en spijkerbroek aangedaan")

print("nu je aangekleed bent kan je kiezen uit en paar schoenen die bij je outfit passen")
print("A = Nike schoenen")
print("B = adidas schoenen ")
print("C = balenciaga schoenen")
antwoord = input()
if antwoord == "A" or antwoord == "a":
    print(" Nice je nike's passen mooi bij je outfit")
elif antwoord == "B" or antwoord == "b":
    print("Nice je adidas schoenen passen mooi bij je outfit")
else:
    print("Nice je balenciaga's passen mooi bij je outfit")

print("kies hoe je naar school zou willen gaan")
print("A = scooter van je broer maar wel zonder rijbewijs.")
print("B = op je fiets")
print("C = met het openbaar vervoer")
antwoord = input()
if antwoord == "A" or antwoord == "a":
    print("je hebt voor de scooter van je broer gekozen maar bent gepakt door de politie")
    print("#############")
    print("#           #")
    print("#   EINDE   #")
    print("#           #")
    print("#############")
elif antwoord == "B" or antwoord == "b":
    print("je bent met je fiets aangekomen. NETJES")
else:
    print("je bent aangekomen op school. NETJES")




