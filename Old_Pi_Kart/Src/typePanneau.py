class typePanneau:
    def __init__(self, idType, forme, libelle, couleur):
        self.idType = idType
        self.forme = forme
        self.libelle = libelle
        self.couleur = couleur

    def __str__(self):
        """Affichage des objets !"""
        return "id Type : {} \n forme : {} \n libelle : {} \n couleur : {} \n".format(
                self.idType, self.forme, self.libelle,self.couleur)
