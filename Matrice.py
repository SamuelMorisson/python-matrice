class Matrice:
    def __init__(self, taille_matrices : tuple):
        self.__taille_matrices = taille_matrices

    def get_matrices(self):
        return self.__taille_matrices
    
    def afficher_matrices(self):
        print("\nAFFICHAGE")
        for matrice in self.__taille_matrices:
            print("------------------------------")
            lignes = []
            for i in range(matrice):
                colonnes = []
                for j in range(matrice):
                    colonnes.append(0)
                lignes.append(colonnes)

            for i in range(len(lignes)):
                print(lignes[i])


    def somme_matrice(self):
        print("\nSOMME")
        somme = 0
        for matrice in self.__taille_matrices:
            somme += matrice
        print("------------------------------")
        lignes = []
        for i in range(somme):
            colonnes = []
            for j in range(somme):
                colonnes.append(0)
            lignes.append(colonnes)
        for i in range(len(lignes)):
            print(lignes[i])


    def multiplication_matrice(self):
        print("\nMULTIPLE")
        multiple = 1
        for matrice in self.__taille_matrices:
            multiple *= matrice
        print("------------------------------")
        lignes = []
        for i in range(multiple):
            colonnes = []
            for j in range(multiple):
                colonnes.append(0)
            lignes.append(colonnes)
        for i in range(len(lignes)):
            print(lignes[i])

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

