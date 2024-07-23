FREECADPATH = '/home/local/CSI/ps45vepo/freecad-python3/lib/'
import sys
sys.path.append(FREECADPATH)
import FreeCAD
doc = FreeCAD.newDocument()
a1 = !a1!                      								#width1 cuboid [mm]
a2 = !a2!										#width2 cuboid [mm]
n = !n!                      	    							#number of cubes in x-direction
m = !m!                      								#number of cubes in y-direction
#b = (38-n*a1)/(n+1)
b = !b!          	    								#distance between cubes in x-direction, [mm]
c = !c!                    	    							#distance between cubes in y-direction, [mm]
y_0 = !y_0!                  	    							#distance of first row of cubes from inlet, [mm]
phi1 = !phi1!										#angle of first rows of cubes
phi2 = !phi2!
angles =[phi1, phi2]
import Part
doc = Part.makeBox(1,1,1)
cube = Part.makeBox(1,1,1)
doc =doc.cut(cube)
for i in range(0, n, 1):
    for j in range(0, m, 1):
        x = (i+1)*b + i*a1
        y = y_0 + j*(a1+c)
        x_m =(i+1)*b + i*a1 + 0.5*a1
        y_m = y_0 + j*(a1+c) + 0.5*a1
        box = Part.makeBox(a1,a2,3)
        box.Placement.Base = FreeCAD.Vector(x, y, 0)
        if j % 2 == 0:
        	box.rotate(App.Vector(x_m, y_m, 0),App.Vector(0, 0, 1), angles[0]) 
        else:
        	box.rotate(App.Vector(x_m, y_m, 0),App.Vector(0, 0, 1), angles[1]) 
        doc = doc.fuse(box)
Part.show(doc)
doc.exportStl("obstacles.stl")
