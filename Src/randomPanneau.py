#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Readerall import readPanneau
import random

def randPan():
    L=readPanneau()
    i=random.randint(0,len(L)-1)
    return L[i]

print "Panneau aleatoire : " +str(randPan())