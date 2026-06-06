#Geometria számológép
#Készítette :Boldizsár Ervin
#version 1.0

import math 


# ----- NÉGYZET -----
def negyzet():
    print("\n")
    oldal = float(input("Add meg a négyzet oldalának hosszát: "))
    terulet = oldal * oldal
    kerület = 4 * oldal
    print("\n")
    print("Négyzet:")
    print("Terület:", terulet)
    print("Kerület:", kerület)

# ----- TÉGLALAP -----
def teglalap():
    print("\n")
    a = float(input("Add meg a téglalap 'a' oldalának hosszát: "))
    b = float(input("Add meg a téglalap 'b' oldalának hosszát: "))
    terulet = a * b
    kerület = 2 * (a + b)
    print("\n")
    print("Téglalap:")
    print("Terület:", terulet)
    print("Kerület:", kerület)

# ----- KÖR -----
def kor():
    print("\n")
    r = float(input("Add meg a kör sugarát: "))
    terulet = math.pi * r * r
    kerület = 2 * math.pi * r
    print("\n")
    print("Kör:")
    print("Terület:", terulet)
    print("Kerület:", kerület)

    # ----- FŐPROGRAM -----
print("Üdvözöl a Geometria számológép!")
print("-------------------------------")

while True:
    print("\nVálassz alakzatot:")
    print("1 - Négyzet")
    print("2 - Téglalap")
    print("3 - Kör")
    print("0 - Kilépés")

    choice = input("Írd be a választott művelet számát: ")

    if choice == '1':
        negyzet()
    elif choice == '2':
        teglalap()
    elif choice == '3':
        kor()
    elif choice == '0':
        print("Viszlát!")
        break
    else:
        print("Érvénytelen választás, kérlek próbáld újra.")
