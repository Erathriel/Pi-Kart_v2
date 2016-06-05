#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
from typePanneau import typePanneau

tree = etree.parse("../xml/Type_Panneaux.xml")
L1 =[]
L2 =[]
for typePanneaux in tree.xpath("/racine/BDD/typePanneaux/typePanneau"):
    for a in typePanneaux.getchildren() :
        L1.append(a.text)

    L2.append(typePanneau(L1[0],L1[1],L1[2],L1[3]))
    del (L1[:])

for i in range (len(L2)) :
    print 'typePanneau'
    print L2[i].idType
    print L2[i].forme
    print L2[i].libelle
    print L2[i].couleur
    print '\n'
