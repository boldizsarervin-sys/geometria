print("Prim számok 1-100-ig \n")

a = 1
kivancsi = 1

while a <= 100:
    seged=2
    osztokSzama = 0    

    while seged < a:
        if a % seged == 0:
            osztokSzama += 1    
            break
        seged +=1

    if osztokSzama == 0:
        print(a, end=", ")
    
    a += 1

print ("\n")

while kivancsi == 1:
    print("\n Írj egy bármilyen számot, amiről tudni akarod, hogy prímszám-e:\n")
    prime = int(input())

    seged = 2
    osztokSzama = 0

    for seged in range(2, prime):
        if prime % seged == 0:
            osztokSzama +=1
            break

    if osztokSzama == 0:
        print("\n┌────────────────────────────────────┐")
        print("│          ! PRÍMSZÁM !              │")
        print("└────────────────────────────────────┘")
    else:
        print("\n┌────────────────────────────────────┐")
        print("│        X NEM PRÍMSZÁM X            │")
        print("└────────────────────────────────────┘")
    
    print("\n┌────────────────────────────────────┐")
    print("│ Kíváncsi vagy másik számra?        │")
    print("│                                    │")
    print("│  [1] IGEN                          │")
    print("│  [2] NEM                           │")
    print("└────────────────────────────────────┘")
    kivancsi = int(input("\nVálasztásod: "))

print("\n Vége!")
input("\nNyomj Enter-t a kilépéshez...")
