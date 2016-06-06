#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
from Panneaux import Panneaux
from typePanneau import typePanneau
import random

<<<<<<< HEAD

def readPanneau():
    tree = etree.parse("../xml/Panneaux.xml")

    L1 =[]
    L2 =[]
    for Panneau in tree.xpath("/racine/BDD/Panneaux/Panneau"):
        for a in Panneau.getchildren() :
           for a in Panneau.getchildren() :
                if (a.text!=None) :
                     L1.append(a.text)
                if (a.get("src")!=None) :
                    L1.append(a.get("src"))
        L2.append(Panneaux(L1[0],L1[1],L1[2],L1[3],L1[4]))
        del (L1[:])

    tree2 = etree.parse("../xml/Type_Panneaux.xml")
    L3 =[]
    L4 =[]
    for typePanneaux in tree2.xpath("/racine/BDD/typePanneaux/typePanneau"):
        for a in typePanneaux.getchildren() :
            L3.append(a.text)

        L4.append(typePanneau(L3[0],L3[1],L3[2],L3[3]))
        del (L3[:])

def readTypePanneau():
    tree2 = etree.parse("../xml/Type_Panneaux.xml")
    L3 =[]
    L4 =[]
    for typePanneaux in tree2.xpath("/racine/BDD/typePanneaux/typePanneau"):
        for a in typePanneaux.getchildren() :
            L3.append(a.text)

        L4.append(typePanneau(L3[0],L3[1],L3[2],L3[3]))
        del (L3[:])
    return L4


def trierContenu(liste, contenu):
    L = []
    for i in range(len(liste)):
        if (liste[i].contenu==contenu):
            L.append(liste[i])
    return L

def trierForme(listeP, listeT, forme) :
    L = []
    idtype = []
    for i in range (len(listeT)) :
        if (listeT[i].forme == forme) :
            idtype.append(listeT[i].idType)
    for i in range(len(listeP)) :
         if (listeP[i].type_id in idtype) :
                    L.append(listeP[i])
    return L

def trierCouleur(listeP, listeT, couleur) :
    L = []
    idtype = []
    for i in range (len(listeT)) :
        if (listeT[i].couleur == couleur) :
            idtype.append(listeT[i].idType)
    for i in range(len(listeP)) :
         if (listeP[i].type_id in idtype) :
                    L.append(listeP[i])
    return L


#print trierContenu(L2," 50 ")
#print trierForme(L2, L4," circulaire ")
#print trierCouleur(L2,L4," Bleu ")


def randPan():
    L=readPanneau()
    i=random.randint(0,len(L)-1)
    return L[i]
