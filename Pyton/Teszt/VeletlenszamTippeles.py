    #random szám kitalálása 1 és 100 között

import random

def szamgeneralas():
    return random.randint(1, 100)

def szamellenorzes():
    while True:
        try:
            ertek = int(input())
            if ertek < 1 or ertek > 100:
                print("Hiba! A számnak 1 és 100 között kell lennie")
            else:
                return ertek
        except ValueError:
            print("Hiba! Számot kell beírni!")


def eredmeny(random_szam, tippelt_szam):
    r = random_szam
    t = tippelt_szam
    if t == r:
        print("Talált!")
        return True
    elif t < r:
        print("Nagyobb")
        return False
    else:
        print("Kisebb")
        return False

def ismétlodes_ellenorzes(tipp, elozo_tippek):
    if tipp in elozo_tippek:
        print("Ez a szám már volt!")

def fo_program():
    veletlenszam = szamgeneralas()
    tippek_szama = 0
    elozo_tippek = []
    print("Adj egy számot 1 és 100 között:")

    while True:
        tipp = szamellenorzes()
        tippek_szama += 1

        if eredmeny(veletlenszam, tipp):
            print(f"\nGratulálok! Eltaláltad a számot {tippek_szama} próbálkozásból.\n")
            print("Tippek: ", elozo_tippek, "\n")
            break
        ismétlodes_ellenorzes(tipp, elozo_tippek)
        elozo_tippek.append(tipp)
        print("\nPróbáld újra!")

fo_program()
