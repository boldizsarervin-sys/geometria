#Geometria számológép
#Készítette :Boldizsár Ervin
#version 1.0

import math 


print("Üdvözöl a Geometria számológép!")
print("-------------------------------")

# ----- NÉGYZET -----
oldal =  float(input("Add meg a négyzet oldalának hosszát: "))
terulet = oldal * oldal
kerulet = 4 * oldal

print("Négyzet:")
print("Oldal hossza:", oldal)
print("Terület:", terulet)
print("Kerület:", kerulet)

# ----- TÉGLALAP -----
a = float(input("Add meg a téglalap 'a' oldalát: "))
b = float(input("Add meg a téglalap 'b' oldalát: "))
terulet = a * b
kerulet = 2 * (a + b)

print("Téglalap:")
print("Terület:", terulet)
print("Kerület:", kerulet)

# ----- KÖR -----
r = float(input("Add meg a kör sugarát: "))
terulet = math.pi * r * r
kerulet = 2 * math.pi * r

print("Kör:")
print("Terület:", terulet)
print("Kerület:", kerulet)

