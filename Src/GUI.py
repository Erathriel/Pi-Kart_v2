# coding: utf8

from Tkinter import *
import Readerall as panneau
from PIL import ImageTk, Image

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

		self.description = Label(self.master, height=100, width=100, bg="light yellow", text="TEST")
		self.description.pack(side=LEFT)

		self.panneautri = Label(self.master, height=20, width=20, bg="light yellow", text="OK")
		self.panneautri.pack(side=TOP)

		self.panneautrif = Label(self.master, height=20, width=20, bg="light yellow", text="OK")
		self.panneautrif.pack(side=TOP)


		self.v = StringVar()
		self.choix = Radiobutton(self.master, text=" Rouge ",variable=self.v, value=" Rouge ")
		self.choix2 = Radiobutton(self.master, text=" Bleu ",variable=self.v, value=" Bleu ")
		self.choix.pack(side=RIGHT)
		self.choix2.pack(side=RIGHT)
		self.choix2.select()

		self.v2 = StringVar()
		self.choixf1 = Radiobutton(self.master, text=" Circulaire ",variable=self.v2, value=" circulaire ")
		self.choixf2 = Radiobutton(self.master, text=" Triangulaire ",variable=self.v2, value=" triangulaire ")
		self.choixf3 = Radiobutton(self.master, text=" Hexagonal ",variable=self.v2, value=" hexagonal ")
		self.choixf1.pack(side=TOP)
		self.choixf2.pack(side=TOP)
		self.choixf3.pack(side=TOP)
		self.choixf1.select()

		self.triercouleur = Button(self.master, text="Tri par couleur", command=self.couleurPanneau, bg="ivory")
		self.triercouleur.pack(side=RIGHT)


		self.trierforme = Button(self.master, text="Tri par forme", command=self.formePanneau, bg="ivory")
		self.trierforme.pack(side=TOP)


		self.image = ImageTk.PhotoImage(Image.open("../images/panneau30.jpg"))
		self.can.create_image(10, 10, image=self.image, anchor='nw')

		self.quitter = Button(self.master, text="Quitter", command=self.quit, bg="ivory")
		self.quitter.pack(side=BOTTOM)
		self.commencer = Button(self.master, text="Afficher un panneau au hasard", command=self.tiragePanneau, bg="ivory")
		self.commencer.pack(side=TOP)


		self.mainloop()

	def tiragePanneau(self):
		Panneau = panneau.randPan()
		self.image = ImageTk.PhotoImage(Image.open("../"+Panneau.images))
		self.can.delete(ALL)
		self.can.create_image(10, 10, image=self.image, anchor='nw')
		self.description['text']  = str(Panneau)

	def couleurPanneau(self):
		couleur = self.v.get()
		L=panneau.readPanneau()
		L2=panneau.readTypePanneau()
		L3=panneau.trierCouleur(L,L2,couleur)
		L1=[]
		for i in range(len(L3)) :
			L1.append(L3[i].nom)
		self.panneautri['text']  = str(L1)
		del (L[:])
		del (L1[:])
		del (L2[:])
		del (L3[:])

	def formePanneau(self):
		forme = self.v2.get()
		L=panneau.readPanneau()
		L2=panneau.readTypePanneau()
		L3=panneau.trierForme(L,L2,forme)
		L1=[]
		for i in range(len(L3)) :
			L1.append(L3[i].nom)
		self.panneautrif['text']  = str(L1)
		print L1
		del (L[:])
		del (L1[:])
		del (L2[:])
		del (L3[:])

test = mainUI()
