#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
from Panneaux import Panneaux


tree = etree.parse("../xml/Panneaux.xml")
L1 =[]
L2 =[]
for Panneau in tree.xpath("/racine/BDD/Panneaux/Panneau"):
    for a in Panneau.getchildren() :
        L1.append(a.text)

    L2.append(Panneaux(L1[0],L1[1],L1[2],L1[3],L1[4]))
    del (L1[:])

for i in range (len(L2)) :
    print 'Panneau'
    print L2[i].id
    print L2[i].nom
    print L2[i].images
    print L2[i].contenu
    print L2[i].type_id

    print '\n'
