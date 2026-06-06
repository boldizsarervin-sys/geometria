import math

class Sikdom:
    def terulet(self):
        return 0

    def kerulet(self):
        return 0

    def info(self):
        print(f"Terület: {self.terulet():.2f}")
        print(f"Kerület: {self.kerulet():.2f}")

class Test:
    def felszin(self):
        return 0

    def terfogat(self):
        return 0

    def info(self):
        print(f"Felszín: {self.felszin():.2f}")
        print(f"Térfogat: {self.terfogat():.2f}")


class Kocka(Test):
    def __init__(self, a):
        self.a = a

    def felszin(self):
        return 6 * self.a * self.a

    def terfogat(self):
        return self.a * self.a * self.a

class Teglatest(Test):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def felszin(self):
        return 2 * (self.a * self.b + self.b * self.c + self.a * self.c)

    def terfogat(self):
        return self.a * self.b * self.c

class Gomb(Test):
    def __init__(self, r):
        self.r = r

    def felszin(self):
        return 4 * math.pi * self.r * self.r

    def terfogat(self):
        return (4/3) * math.pi * self.r * self.r * self.r

class Henger(Test):
    def __init__(self, r, m):
        self.r = r
        self.m = m

    def felszin(self):
        return 2 * math.pi * self.r * (self.r + self.m)

    def terfogat(self):
        return math.pi * self.r * self.r * self.m

def bekер_szamot(szoveg):
    while True:
        try:
            ertek = float(input(szoveg))
            if ertek <= 0:
                print("Hiba! Pozitív számot kell beírni!")
            else:
                return ertek
        except ValueError:
            print("Hiba! Számot kell beírni!")

def menu():
    print("Üdvözöl a Geometriai Számológép!")
    print("----------------------------------")

    while True:
        print("\nVálassz alakzatot:")
        print("1 - Kocka")
        print("2 - Téglatest")
        print("3 - Gömb")
        print("4 - Henger")
        print("0 - Kilépés")

        valasztas = input("Választásod: ")

        if valasztas == "1":
            a = bekер_szamot("Add meg az oldalt: ")
            Kocka(a).info()

        elif valasztas == "2":
            a = bekер_szamot("Add meg az 'a' oldalt: ")
            b = bekер_szamot("Add meg a 'b' oldalt: ")
            c = bekер_szamot("Add meg a 'c' oldalt: ")
            Teglatest(a, b, c).info()

        elif valasztas == "3":
            r = bekер_szamot("Add meg a sugarat: ")
            Gomb(r).info()

        elif valasztas == "4":
            r = bekер_szamot("Add meg a sugarat: ")
            m = bekер_szamot("Add meg a magasságot: ")
            Henger(r, m).info()

        elif valasztas == "0":
            print("Viszlát!")
            break

        else:
            print("Érvénytelen választás!")

menu()