class Voiture:  # Def de la classe Voiture
    """docstring for Voiture
	Definie par :
		- Sa vitesse
		- Sa trajectoire
		- Son etat"""

	def __init__(self, vitesse, trajectoire, etat):
        """ Constructeur """
        self.vitesse = vitesse
        self.trajectoire = trajectoire
        self.état = etat