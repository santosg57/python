#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys
 
print "Número de parámetros: ", len(sys.argv)
print "Lista de argumentos: ", sys.argv

par = sys.argv[1]

print dir(par)
