print("Adja meg a teglatest adatait: a \n")

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))

terfogat = A * B * C
felszin = (A*B + A*C + B*C) * 2

print(f"\nA teglatest terfogata: {terfogat}")
print(f"A teglatest felszine: {felszin}\n")

input("Nyomj Enter-t a kilépéshez...")
