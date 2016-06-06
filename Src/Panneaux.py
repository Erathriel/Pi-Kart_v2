class Panneaux:  # Def de la classe Panneaux
    """docstring for Panneaux
	Definie par :
		- Son id
		- Son nom
		- Son le chemin de son images
		- Son contenu
		- Son type"""

    def __init__(self, id, nom, images, contenu, type_id):
        """ Constructeur """
        self.id = id
        self.nom = nom
        self.images = images
        self.contenu = contenu
        self.type_id = type_id

    def __str__(self):
        """Affichage des objets !"""
        return " id : {} \n nom : {} \n images : {} \n contenu : {} \n type : {} \n".format(
                self.id, self.nom, self.images,self.contenu,self.type_id)
