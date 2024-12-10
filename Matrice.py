class Matrice:
    def __init__(self, matrice : list):

        length_matrice = len(matrice)
        matrice_carre = True
        for i in matrice:
            if len(i) != length_matrice:
                matrice_carre = False
        if matrice_carre == True:
            self.__matrice = matrice
        else:
            self.__matrice = None


    def get_matrice(self):
        return self.__matrice
    

    def __str__(self):
        if self.__matrice != None:
            print("\nAFFICHAGE")
            for line in self.__matrice:
                print(line)
        else:
            print("Cette matrice n'est pas carrée")


    def __add__(self, autre_matrice):
        # Vérifie que les matrices ne soit pas vide et de même taile
        if self.__matrice != None and autre_matrice.get_matrice() != None:
            if len(self.__matrice) == len(autre_matrice.get_matrice()):
                
                # Créé un mnouvelle matrice remplie de 0 de la taille des 2 autres matrices
                somme_matrices = []
                for i in range(len(self.__matrice)):
                    ligne = []
                    for j in range(len(self.__matrice)):
                        ligne.append(0)
                    somme_matrices.append(ligne)

                # Somme des matrices
                for line in range(len(self.__matrice)):
                    for column in range(len(self.__matrice)):
                        somme_matrices[line][column] = self.__matrice[line][column] + autre_matrice.get_matrice()[line][column]
                        #print(somme_matrices)

                # Affichage de la somme des 2 matrices
                print("\nSOMME")
                for line in somme_matrices:
                    print(line)


    def __mul__(self, autre_matrice):
        matrice_multiple = []

        # Créé un mnouvelle matrice remplie de 0 de la taille des 2 autres matrices
        for i in range(len(self.__matrice)):
            ligne = []
            for j in range(len(self.__matrice)):
                ligne.append(0)
            matrice_multiple.append(ligne)

        # Fait la multiplication des 2 matrcies en changeant chacune des valeurs de la nouvelle
        for line in range(len(self.__matrice)):
            for column in range(len(self.__matrice)):
                value = 0
                for n in range(len(self.__matrice)):
                    value += (self.__matrice[line][n]) * (autre_matrice.get_matrice()[n][column])
                matrice_multiple[line][column] = value

        # Affiche le résultat
        print("\nMULTIPLICATION")
        for line in matrice_multiple:
                    print(line)





matrice1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrice2 = [
    [9, 2, 5],
    [8, 6, 3],
    [1, 4, 7]
]
objetMatrice1 = Matrice(matrice1)
objetMatrice2 = Matrice(matrice2)
objetMatrice1.__str__()
objetMatrice1.__add__(objetMatrice2)
objetMatrice1.__mul__(objetMatrice2)