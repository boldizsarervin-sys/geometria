import math

class Sikdom:
    def terulet(self):
        return 0

    def kerulet(self):
        return 0

    def info(self):
        print(f"Terület: {self.terulet():.2f}")
        print(f"Kerület: {self.kerulet():.2f}")

class Negyzet(Sikdom):
    def __init__(self, oldal):
        self.oldal = oldal

    def terulet(self):
        return self.oldal * self.oldal

    def kerulet(self):
        return 4 * self.oldal

class Teglalap(Sikdom):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def terulet(self):
        return self.a * self.b

    def kerulet(self):
        return 2 * (self.a + self.b)

class Kor(Sikdom):
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

        valasztas = input("Választásod: ")

        if valasztas == "1":
            while True:
                try:
                    oldal = float(input("Add meg az oldalt: "))
                    break
                except ValueError:
                    print("Hibás bemenet! Számot kell beírni.")
            n = Negyzet(oldal)
            n.info()

        elif valasztas == "2":
            while True:
                try:
                    a = float(input("Add meg az 'a' oldalt: "))
                    b = float(input("Add meg a 'b' oldalt: "))
                    break
                except ValueError:
                    print("Hibás bemenet! Számot kell beírni.")
            t = Teglalap(a, b)
            t.info()

        elif valasztas == "3":
            while True:
                try:
                    r = float(input("Add meg a sugarat: "))
                    break
                except ValueError:
                    print("Hibás bemenet! Számot kell beírni.")
            k = Kor(r)
            k.info()

        elif valasztas == "0":
            print("Viszlát!")
            break

        else:
            print("Érvénytelen választás!")

menu()

