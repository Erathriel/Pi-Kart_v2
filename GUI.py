class mainUI(Frame):
	"""docstring for mainUI"""
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.start()

	def start(self):
		"""Fonction éxécutée à la création de la fenètre, on affiche le canvas, les boutons pour accéder aux différentes boites de dialogue (saisie du polygone, création de
			la matrice de transformation. On initialise les différentes variables du programme, et on lance la boucle de tkinter."""
		self.master.title('Affichage des figures')
		self.master.configure(width=700, height=500, bg="ivory")
		self.can = Canvas(self.master, height=400, width=400, bg="light yellow", cursor="trek")
		self.can.pack(side=LEFT)
		self.traceRepere()
		self.quitter = Button(self.master, text="Quitter", command=self.quit, bg="ivory")
		self.quitter.pack(side=BOTTOM)
		self.commencer = Button(self.master, text="Éditer le polygone", command=self.askUserP, bg="ivory")
		self.commencer.pack(side=TOP)
		self.transformer = Button(self.master, text="Éditer la transformation", command=self.askUserT, bg="ivory")
		self.transformer.pack(side=TOP)
		self.drawB = Button(self.master, text="Figure de base", command=self.drawBase, bg="ivory")
		self.drawB.pack(side=TOP)
		self.drawT = Button(self.master, text="Figure transformée", command=self.drawTrans, bg="ivory")
		self.drawT.pack(side=TOP)
		self.demo = Button(self.master, text="Démonstration", command=self.interactivite, bg="ivory")
		self.demo.pack(side=TOP)

		self.matriceTransfo = []
		self.matriceFinale = []
		self.transformRadio=IntVar()
		self.figureBase = createFigure()
		self.figureTrans = createFigure()
		self.oldFigure = []
		self.polygone = []
		self.mainloop()


	def traceRepere(self):
		"""Fonction qui permet de tracer le repère dans le canvas, elle trace également un cadrillage."""

		for i in xrange(0,41):
			self.can.create_line(i*10, 0, i*10, 400, fill="yellow")
			self.can.create_line(0, i*10, 400, i*10, fill="yellow")

		self.can.create_line(0, 200, 400, 200, fill ='orange')
		self.can.create_line(200, 400, 200, 0, fill ='orange')

	def coordPoint(self, valeur, x=True):
		"""Fonction qui corrige les coordonnées pour centrer le (0,0) sur le canvas."""
		if x:
			return valeur + 200
		else:
			return 200 - valeur

	def drawBase(self):
		"""Fonction qui dessine la figure entrée par l'utilisateur"""
		self.traceFigure(self.figureBase)

	def drawTrans(self):
		"""Fonction qui affiche la figure transformée par la matrice"""
		self.traceFigure(self.figureTrans)

	def traceLigne(self, pointa, pointb):
		"""trace une ligne sur le Canvas en prenant en compte que (0,0) est au centre de ce dernier"""
		self.can.create_line(self.coordPoint(pointa[0]), self.coordPoint(pointa[1], False), self.coordPoint(pointb[0]), self.coordPoint(pointb[1], False), fill='black')

	def tracePoly(self, poly):
		"""Trace les lignes entre tous les points d'un polygone"""
		for j in xrange(1,len(poly)):
			self.traceLigne(poly[j-1], poly[j])
		self.traceLigne(poly[0], poly[-1])

	def traceFigure(self, figure, clear=True):
		"""Trace la figure. Si clear vaut True, on nettoie le canvas et on retrace le repère, sinon on écrit par dessus."""
		if clear :
			self.can.delete(ALL)
			self.traceRepere()
		for j in xrange(0,len(figure)):
			self.tracePoly(figure[j])
		self.update()


test = mainUI()
