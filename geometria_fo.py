import math

# ========================
# ŐS OSZTÁLYOK
# ========================

class Sikdom:
    def terulet(self):
        return 0

    def kerulet(self):
        return 0

    def info(self):
        print(f"  Terület: {self.terulet():.2f}")
        print(f"  Kerület: {self.kerulet():.2f}")

class Test:
    def felszin(self):
        return 0

    def terfogat(self):
        return 0

    def info(self):
        print(f"  Felszín: {self.felszin():.2f}")
        print(f"  Térfogat: {self.terfogat():.2f}")

# ========================
# SÍKIDOMOK
# ========================

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

# ========================
# 3D TESTEK
# ========================

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

# ========================
# SEGÉDFÜGGVÉNY
# ========================

def beker_szamot(szoveg):
    while True:
        try:
            ertek = float(input(szoveg))
            if ertek <= 0:
                print("  Hiba! Pozitív számot kell beírni!")
            else:
                return ertek
        except ValueError:
            print("  Hiba! Számot kell beírni!")

# ========================
# FŐPROGRAM
# ========================

def menu():
    print("╔══════════════════════════════╗")
    print("║   Geometriai Számológép      ║")
    print("╚══════════════════════════════╝")

    while True:
        print("\n── Főmenü ──")
        print("  1 - Síkidomok")
        print("  2 - 3D Testek")
        print("  0 - Kilépés")

        valasztas = input("\nVálasztásod: ")

        if valasztas == "1":
            menu_sikdomok()

        elif valasztas == "2":
            menu_3d()

        elif valasztas == "0":
            print("\nViszlát!")
            break

        else:
            print("  Érvénytelen választás!")

def menu_sikdomok():
    while True:
        print("\n── Síkidomok ──")
        print("  1 - Négyzet")
        print("  2 - Téglalap")
        print("  3 - Kör")
        print("  0 - Vissza")

        valasztas = input("\nVálasztásod: ")

        if valasztas == "1":
            oldal = beker_szamot("Add meg az oldalt: ")
            Negyzet(oldal).info()

        elif valasztas == "2":
            a = beker_szamot("Add meg az 'a' oldalt: ")
            b = beker_szamot("Add meg a 'b' oldalt: ")
            Teglalap(a, b).info()

        elif valasztas == "3":
            r = beker_szamot("Add meg a sugarat: ")
            Kor(r).info()

        elif valasztas == "0":
            break

        else:
            print("  Érvénytelen választás!")

def menu_3d():
    while True:
        print("\n── 3D Testek ──")
        print("  1 - Kocka")
        print("  2 - Téglatest")
        print("  3 - Gömb")
        print("  4 - Henger")
        print("  0 - Vissza")

        valasztas = input("\nVálasztásod: ")

        if valasztas == "1":
            a = beker_szamot("Add meg az oldalt: ")
            Kocka(a).info()

        elif valasztas == "2":
            a = beker_szamot("Add meg az 'a' oldalt: ")
            b = beker_szamot("Add meg a 'b' oldalt: ")
            c = beker_szamot("Add meg a 'c' oldalt: ")
            Teglatest(a, b, c).info()

        elif valasztas == "3":
            r = beker_szamot("Add meg a sugarat: ")
            Gomb(r).info()

        elif valasztas == "4":
            r = beker_szamot("Add meg a sugarat: ")
            m = beker_szamot("Add meg a magasságot: ")
            Henger(r, m).info()

        elif valasztas == "0":
            break

        else:
            print("  Érvénytelen választás!")

menu()
