#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 17:47:10 2020

@author: akel
Programa teste com entradas para modelagem MT3D

"""
#import matplotlib.pyplot as plt

import argparse
import NMT3D as model
import loadmigeo as load  #
import pyvista as pv
import vtk

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

plt.close('all')

print('Running geofem test')

#plt.close('all')

##usando o spyder! (decomentar para usar)
out=load.inputfiles('MT3D_input_ex3.in') #função

#usando o terminal!(decomentar para usar.)
#parser = argparse.ArgumentParser()
#parser.add_argument("inp", help="input file",type=str)
#ARG = parser.parse_args()
#out=load.inputfiles(ARG.inp)


#se não declarado opt=='tensor' o código execultar mesh octree
Me,cond=model.modelmesh(out,level=1) #run octree mesh

#informações da malha em tela
print("\n the mesh has {} cells".format(Me))
print("\n the mesh has {} cells".format(Me.nC))


#plot matplotlib
fig,a1 = plt.subplots(num=1,clear=True)
pcoloropts = {"cmap":"spring"}
fig.canvas.set_window_title('Slice Y')
cb=Me.plotSlice(np.log10(cond), grid=True, normal='y',ax=a1)
fig.colorbar(cb[0],ax=a1)

#
fig,a2 = plt.subplots(num=2,clear=True)
fig.canvas.set_window_title('Slice X')
cb2=Me.plotSlice(np.log10(cond), grid=True, normal='x',ax=a2)
fig.colorbar(cb2[0],ax=a2)


# vizualizar via pyvista
model.pyvista_view(out)
