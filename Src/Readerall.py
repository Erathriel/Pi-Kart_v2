#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
from Panneaux import Panneaux
from typePanneau import typePanneau
import random

def readPanneau():
    tree = etree.parse("../xml/Panneaux.xml")
    L1 =[]
    L2 =[]
    for Panneau in tree.xpath("/racine/BDD/Panneaux/Panneau"):
        for a in Panneau.getchildren() :
            L1.append(a.text)

        L2.append(Panneaux(L1[0],L1[1],L1[2],L1[3],L1[4]))
        del (L1[:])
    return L2

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

L2 = readPanneau()
L4 = readTypePanneau()

def trierContenu(liste, contenu):
    L = []
    s=""
    for i in range(len(liste)):
        if (liste[i].contenu==contenu):
            L.append(liste[i])
    for i in L :
        s += str(i)
    print(s)
    return L

def trierForme(listeP, listeT, forme) :
    L = []
    idtype = []
    s=""
    for i in range (len(listeT)) :
        if (listeT[i].forme == forme) :
            idtype.append(listeT[i].idType)
    for i in range(len(listeP)) :
         if (listeP[i].type_id in idtype) :
                    L.append(listeP[i])
    for i in L :
        s += str(i)
    print(s)
    return L

def trierCouleur(listeP, listeT, couleur) :
    L = []
    s=""
    idtype = []
    for i in range (len(listeT)) :
        if (listeT[i].couleur == couleur) :
            idtype.append(listeT[i].idType)
    for i in range(len(listeP)) :
         if (listeP[i].type_id in idtype) :
                    L.append(listeP[i])
    for i in L :
        s += str(i)
    print(s)
    return L

def randPan():
    L=readPanneau()
    i=random.randint(0,len(L)-1)
    return L[i]
