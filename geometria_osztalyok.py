import math

class Negyzet:
    def __init__(self, oldal):
        self.oldal = oldal

    def terulet(self):
        return self.oldal * self.oldal

    def kerulet(self):
        return 4 * self.oldal

class Teglalap:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def terulet(self):
        return self.a * self.b

    def kerulet(self):
        return 2 * (self.a + self.b)

class Kor:
    def __init__(self, r):
        self.r = r

    def terulet(self):
        return math.pi * self.r * self.r

    def kerulet(self):
        return 2 * math.pi * self.r


def menu():
    print("Üdvözöl a Geometria számológép!")
    print("----------------------------------")

    while True:
        print("\nVálassz alakzatot:")
        print("1 - Négyzet")
        print("2 - Téglalap")
        print("3 - Kör")
        print("0 - Kilépés")

        valasztas = input("Válaszdtásod: ")

        if valasztas == '1':
            oldal = float(input("Add meg az oldalt: "))
            n = Negyzet(oldal)
            print(f"Terület: {n.terulet():.2f}")
            print(f"Kerület: {n.kerulet():.2f}")

        elif valasztas == '2':
            a = float(input("Add meg az 'a' oldalt: "))
            b = float(input("Add meg a 'b' oldalt: "))
            t = Teglalap(a, b)
            print(f"Terület: {t.terulet():.2f}")
            print(f"Kerület: {t.kerulet():.2f}")

        elif valasztas == '3':
            r = float(input("Add meg a sugár: "))
            k = Kor(r)
            print(f"Terület: {k.terulet():.2f}")
            print(f"Kerület: {k.kerulet():.2f}")    

        elif valasztas == '0':
            print("Viszlát!")
            break

        else:
            print("Érvénytelen választás. Próbáld újra.")

menu()

