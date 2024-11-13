'''
Gissa-talet.PY: Ett spel där man gissar ett hemligt tal som är slumpmässigt. talet är mellan 1-100.

__author__  = "Ludvig Hellström"
__version__ = "1.0.0"
__email__   = "ludvig.hellstrom@elev.ga.ntig.se"
'''

print("VÄLKOMMEN TILL SPELET SOM HETER: GISSA TALET")
print("Målet är att gissa talet som har generarats")

from random import randint

while True:
    hidden_number = randint(1 ,100) 

    i = 1
    while i < 8:
        i += 1
        try:   #Jag har gjort att man måste skriva in tal.
            guess = int(input("gissa talet: "))     
        except Exception as error_code:
            print("snälla skriv siffror")
            continue
        
        if guess == hidden_number:
            total_guesses = (i - 1)     #Den här beräkningen visar hur många fösök det tog.
            print(f"Du hittade talet som var: {hidden_number} på {total_guesses} försök")
            break

        elif guess > hidden_number:
            print(f"för högt - prova igen (du har {8 - i} försök kvar)") #visar försök kvar

        elif guess < hidden_number:
            print(f"för lågt - prova igen (du har {8 - i} försök kvar)")
        
    value = input("vill du spela igen? (ja/nej): ")
    if value == "n":
        exit()
    if value == "nej":
        exit()
    if value == "j":
        continue
    if value == "ja":
        continue
