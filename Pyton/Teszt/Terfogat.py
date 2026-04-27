# Dictionary

menuk = {
    "fo": ('1','2','q')
}




def terulet_negyzet(A):
    ter = A * A
    ker = A * 4
    return ter, ker

def kerulet_negyzet (A):
    return A * 4

def terulet_teglalap (A,B):
    return A * B

def terulet_kor (r):
    return r**2*3.14



def kerulet_teglalp (A,B):
    return A * 2 + B * 2

def kerulet_kor (r):
    return 2 * r * 3.14

def kerdes ():
    print()
    return input("Válassz: ")
    
def normalizalas (valasz):
    return str(valasz).lower()

def ellenorzes (bemenet, *valaszthato):
    for v in valaszthato:
        if bemenet == v:
            return bemenet
    return 'ervenytelen'


#############
# Kiirások  #
#############

#Üdvözlés

def udvozles():
    print()
    print("#" * 50)
    print()
    print("""\t Üdvözlet! 
    \t Ez az első Python programom. \n 
    \t Sikidomok területét, kerületét és
    \t testek térfogatát, felületét lehet vele kiszámoltatni.""")
    print()
    print("#"*50)
    print()

# Elágazás 2D vagy 3D

def kiiras_2d_vagy_3d ():
    print()
    print ("2D (1)")
    print ("3D (2)")
    print("kilépés (q)")


# Elágazás 2D formák

def kiiras_2D_formak ():
    print("Kör (1)")
    print("Négyzet (2)")
    print("Téglalap (3)")
    return input("Válassz:")

###################################### Főprogram ####################


def foprogram():
    
    udvozles()

    valasz='ervenytelen'

    while valasz=='ervenytelen':
        kiiras_2d_vagy_3d()
        valasz = kerdes()
        valasz = normalizalas(valasz)
        valasz=ellenorzes(valasz,*menuk["fo"])





    print (" Vege")



if __name__ == "__main__":
    foprogram()
    

