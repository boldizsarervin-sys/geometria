print("Prímszámok 1-100")

a = 1
while a <= 100:
    seged = 2
    osztokSzama = 0
    
    while seged < a:
        if a % seged == 0:
            osztokSzama += 1
        seged += 1
    
    if osztokSzama == 0:
        print(a, end=", ")
    
    a += 1

print("\n")

kivancsi = 1

while kivancsi == 1:
    print("\nÍrj egy bármilyen számot, amiről tudni szeretnéd, hogy prímszám-e:")
    prime = int(input())
    
    seged = 2
    osztokSzama = 0
    
    for seged in range(2, prime):
        if prime % seged == 0:
            osztokSzama += 1
    
    if osztokSzama == 0:
        print("\n┌────────────────────────────────────┐")
        print("│          ! PRÍMSZÁM !              │")
        print("└────────────────────────────────────┘")
    else:
        print("\n┌────────────────────────────────────┐")
        print("│        X NEM PRÍMSZÁM X            │")
        print("└────────────────────────────────────┘")
    
    print("\nKíváncsi vagy másik számra?")
    print(" 1 - igen")
    print(" 2 - nem")
    kivancsi = int(input("\nVálasztásod: "))

print("\nVége!")
input("\nNyomj Enter-t a kilépéshez...")