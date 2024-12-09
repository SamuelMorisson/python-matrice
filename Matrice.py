class Matrice:
    def __init__(self, taille_matrices : tuple):
        self.__taille_matrices = taille_matrices

    def get_matrices(self):
        return self.__taille_matrices
    
    def afficher_matrices(self):
        print("\nAFFICHAGE")
        for matrice in self.__taille_matrices:
            print("------------------------------")
            a = []
            for i in range(matrice):
                b = []
                for j in range(matrice):
                    b.append(0)
                a.append(b)

            for i in range(len(a)):
                print(a[i])


    def somme_matrice(self):
        print("\nSOMME")
        somme = 0
        for matrice in self.__taille_matrices:
            somme += matrice
        print("------------------------------")
        a = []
        for i in range(somme):
            b = []
            for j in range(somme):
                b.append(0)
            a.append(b)
        for i in range(len(a)):
            print(a[i])


    def multiplication_matrice(self):
        print("\nMULTIPLE")
        multiple = 1
        for matrice in self.__taille_matrices:
            multiple *= matrice
        print("------------------------------")
        a = []
        for i in range(multiple):
            b = []
            for j in range(multiple):
                b.append(0)
            a.append(b)
        for i in range(len(a)):
            print(a[i])

'''listeTest : tuple = (2, 4)
test = Matrice(listeTaille)
test.afficher_matrices()
test.somme_matrice()
test.multiplication_matrice()'''

matricesTest = (3, 3)
listeMatrice = Matrice(matricesTest)
listeMatrice.afficher_matrices()
listeMatrice.somme_matrice()
listeMatrice.multiplication_matrice()

