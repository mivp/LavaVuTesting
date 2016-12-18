#!/usr/bin/env python
import lavavu

#This test ensures legacy viewport support in image output works correctly
#Same test is run using three different image output methods to verify
# all these pathways produce the same output

dbfile = "uw1-vp-gLucifer.gldb"

#Using image output scripted through python 
#(NOTE: something weird happens if this runs last, so moved to first)
lv = lavavu.Viewer(quality=3, port=0)
lv.file(dbfile)

lv.open()

for ts in range(300,501,100):
    lv.timestep(ts)
    lv.image("window-" + str(ts).zfill(5))

lv.testimages()

#Using automated image output
lv = lavavu.Viewer(writeimage=True, timestep=[300, 500], database=dbfile, figure=-1, quality=3, port=0)

lv.testimages(clear=True)

#Again using "images" command
lv = lavavu.Viewer(database=dbfile, quality=3, port=0)
lv.timestep(300)
lv.images(500)
lv.testimages(clear=True)
lv.clear()


