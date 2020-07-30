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
import loadmigeo as load #contem arquivos de input
import pyvista as pv

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

plt.close('all')

print('Running geofem test')

#plt.close('all')

##usando o spyder! 
#out=load.inputfiles('MT3D_input_ex2.in')


#usando o terminal!
parser = argparse.ArgumentParser()
parser.add_argument("inp", help="input file",type=str)
ARG = parser.parse_args()
out=load.inputfiles(ARG.inp)
#print(out['box'])
Me,cond=model.MT3D(out,opt='tensor')



 ##plot matplotlib
#fig,axes = plt.subplots(num=1,clear=True)
#Me.plotSlice(np.log(cond), grid=True, normal='y',ax=axes)
#
#plt.show()



#plot pyvista
models = {'res': np.log(cond)}
dataset = Me.toVTK(models)

#grid=Me.toVTK(models)
#p = pv.Plotter(notebook=0)
#p.add_mesh(grid.wireframe())
#p.show()
#
#
p = pv.Plotter(notebook=0)
p.show_grid(location='outer')
#
#
p.add_mesh(dataset.slice('x'), opacity=0.75, name='x-slice')
p.add_mesh(dataset.slice('y'), opacity=0.75, name='y-slice')
p.add_mesh(dataset.slice('z'), opacity=0.75, name='z-slice')

p.show()




