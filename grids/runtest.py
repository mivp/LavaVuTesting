#!/usr/bin/env python
# coding: utf-8
#Test grid/quads plotting by creating the same image in several ways

#note: quads renderer accepts vertices as actual quads or a grid (with dims provided)
# quads are defined by four vertices traversed counter-clockwise
# grids are defined from top left (eg: x=0, y=1.0), row by row

import lavavu
#lv = lavavu.Viewer(background="white", border=0, axis=False)
#quads = lv.quads("mesh", cullface=True)

import random
random.seed(0) # Set the random number generator to a fixed sequence.

#Create viewer
lv = lavavu.Viewer(background="white", border=0, axis=False, resolution=(300,300)) #, verbose=True)
quads = None

def createGrid(verts, indices=None, colours=None, dims=None, flat=True, tris=False, **kwargs):
    global lv, quads

    #Clear all data
    if quads:
        lv.clear(True)
        for key in kwargs:
            quads[key] = kwargs[key]

    if tris:
        quads = lv.mesh("mesh", cullface=True, flat=True, dims=[0,0], **kwargs)
    else:
        quads = lv.quads("mesh", cullface=True, flat=flat, dims=dims, **kwargs)

    quads.colourmap("diverge");
    quads["colourby"] = "field"
    quads.vertices(verts)
    #Test colour vals
    vals = [random.uniform(-0.5,0.5), random.uniform(-0.5,0.5), random.uniform(-0.5,0.5), random.uniform(-0.5,0.5)]
    if colours is None:
        quads.values(vals, "field")
    else:
        quads.colours(colours)
    if indices is not None:
        quads.indices(indices)
    lv.display()
    #lv.interactive()

#1)
V = lavavu.grid2d(dims=[3,3])
print(V)
print(V.shape)
createGrid(V)

#2)
V = lavavu.grid3d(dims=[3,3])
print(V)
print(V.shape)

createGrid(V)

# Create some quads in a python list
# - just provide vertices, no grid dimensions so will expect counter-clockwise quad vertex ordering
def quad2(minv, maxv):
    #Generate using two triangles - actual quads are no longer supported
    return [[minv, [maxv[0], minv[1]], maxv], [minv, maxv, [minv[0], maxv[1]]]]
corners = []
corners += quad2([0,0], [1,1])
corners += quad2([1,0], [2,1])
corners += quad2([0,1], [1,2])
corners += quad2([1,1], [2,2])

#3) Draw with vertices only
createGrid(corners, tris=True)

#    0       1      2      3      4      5      6      7      8
V = [[0,2], [1,2], [2,2], [0,1], [1,1], [2,1], [0,0], [1,0], [2,0]]
#I = [[3, 4, 1, 0], [4, 5, 2, 1], [6, 7, 4, 3], [7, 8, 5, 4]]
I = [[3, 4, 1], [1, 0, 3], [4, 5, 2], [2, 1, 4], [6, 7, 4], [4, 3, 6], [7, 8, 5], [5, 4, 7]]

#4) Use our own indices - colours will be interpolated
colourlist = ["#ff0000", "#880000", "#000000", "#ff8800", "#888800", "#008800", "#ffff00", "#88ff00", "#00ff00"]
createGrid(V, I, colours=colourlist, flat=False)

#5) With passed dims, auto index, grid layout expected:
createGrid(V, None, dims=[3,3])

#6) With calculated dims
V = [[[0,2], [1,2], [2,2]], [[0,1], [1,1], [2,1]], [[0,0], [1,0], [2,0]]]
createGrid(V)

#Compare the output to expected results
lv.testimages()

