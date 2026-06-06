#Geometria számológép
#Készítette :Boldizsár Ervin
#version 1.0

import math 


# ----- NÉGYZET -----
def negyzet():
    oldal = float(input("Add meg a négyzet oldalának hosszát: "))
    terulet = oldal * oldal
    kerület = 4 * oldal
    print("\n")
    print("Négyzet:")
    print("Terület:", terulet)
    print("Kerület:", kerület)

# ----- TÉGLALAP -----
def teglalap():
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
print("\n")
negyzet()
print("\n")
teglalap()
print("\n")
kor()
