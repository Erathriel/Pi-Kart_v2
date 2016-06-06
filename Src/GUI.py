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

		self.image = ImageTk.PhotoImage(Image.open("../images/panneau30.jpg"))
		self.can.create_image(10, 10, image=self.image, anchor='nw')

		self.quitter = Button(self.master, text="Quitter", command=self.quit, bg="ivory")
		self.quitter.pack(side=BOTTOM)
		self.commencer = Button(self.master, text="Afficher un panneau au hasard", command=self.tiragePanneau, bg="ivory")
		self.commencer.pack(side=TOP)

		self.mainloop()

	def tiragePanneau(self):
		Panneau = panneau.randPan()
		self.description['text']  = str(Panneau)

test = mainUI()
