import random

isRunning = True

while (isRunning == True):
        print("herhaal")
        if (random.randint(0,2) == 1 ):
            isRunning = False
else:
    print("doe als laatste dit")


print("einde programma")

# index      0     1    2     3
lijstA = ["tekst", 1, True, 44.05]
lijstB = ["dit, "is", "een", "reeks", "tekst"]

print(lijstA)
print( lijstA[3] )

print(lijstB)
lijstB[1] = "VERANDERD"
print(lijstB)

# door lijstB heen gssn
for waarde in lijstB:
    print("Dit is waarde:", waarde)


lijstGROOTTE = len(lijstA)
print("lijstA is", lijstGROOTTE, "lang")

for waarde in lijstB:
    waarde = "iets"
    print(waarde)

print(lijstB)

for waarde in range(5):
    print("leuk, waarde is", waarde)

for waarde in range(len(lijstB) ):
    if (lijstB[waarde] == "reeks"):
        lijstB[waarde] = "reeks is VERANDERD"
    print(lijstB[waarde])

print(lijstB)



objects = [ "Viool", "Bal", "Beker", "Tafel" ]
 print(objects)

for obj in range( len( objects ) ) : # Zoek en verwijder de bal

    print(obj)
   if ( objects[ index ] == "Bal" ) : # Gevonden! Stop met zoeken…
       objects[ index ] = ""
       break


print("Bal verwijderd! (Leeg gemaakt.)")
print(objects)























        
