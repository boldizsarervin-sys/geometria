def prim_e(szam):
    """
    Megnézi, hogy egy szám prím-e.
    Visszatérési érték: True ha prím, False ha nem.
    """
    if szam < 2:
        return False, None
    
    # Elég a négyzetgyökig ellenőrizni (gyorsabb!)
    for i in range(2, int(szam**0.5) + 1):
        if szam % i == 0:
            legkisebbOszto = i # Nem prim esetén megmutatja a legkisebb osztót
            return (False, legkisebbOszto)  # Van osztója, nem prím
    
    return (True, None)  # Nincs osztója, prím!


def primek_listazasa(tol, ig):
    """
    Kilistázza a prímszámokat egy adott tartományban.
    """
    primek = []
    
    for szam in range(tol, ig + 1):
        prim, _ = prim_e(szam)
        if prim:
            primek.append(szam)
    
    return primek


def fo_program():
    """
    A program fő része - prímek listázása és user által megadott szám ellenőrzése.
    """
    print("=" * 50)
    print("PRÍMSZÁM ELLENŐRZŐ PROGRAM")
    print("=" * 50)
    
    # 1. Prímek listázása 1-100-ig
    print("\nPrímszámok 1 és 100 között:")
    primek = primek_listazasa(1000, 2500)
    print(", ".join(map(str, primek)))
    print(f"\nÖsszesen {len(primek)} darab prímszám van 1 és 100 között.\n")
    
    # 2. User által megadott számok ellenőrzése
    print("-" * 50)
    print("Írj be egy számot a vizsgálathoz, vagy 'q'-t a kilépéshez!")
    print("-" * 50)
    
    while True:
        bemenet = input("\nSzám (vagy 'q' a kilépéshez): ")
        
        # Kilépés ellenőrzése
        if bemenet.lower() == 'q':
            break
        
        # Szám ellenőrzése
        try:
            szam = int(bemenet)
            
            prim, oszto =prim_e(szam)

            if prim:
                print("\n┌────────────────────────────────────┐")
                print("│          ! PRÍMSZÁM !              │")
                print("└────────────────────────────────────┘")
            else:
                print("\n┌────────────────────────────────────┐")
                print("│         X NEM PRÍMSZÁM X           │")
                print("└────────────────────────────────────┘")
                print(f"A legkisebb osztó: {oszto}")
        
        except ValueError:
            print("Hibás bemenet!")
    
    print("\n" + "=" * 50)
    print("Köszönöm, hogy használtad a programot!")
    print("=" * 50)


# Program indítása
if __name__ == "__main__":
    fo_program()