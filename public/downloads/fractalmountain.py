import turtle
import random

# ***** Triangle class keeps track of 3 indices in pointMap, p1, p2, p3 *****
class Triangle:
	def __init__(self, p1, p2, p3):
		self.pts = []
		self.pts.append(p1)
		self.pts.append(p2)
		self.pts.append(p3)

	def p1(self):
		return self.pts[0]

	def p2(self):
		return self.pts[1]

	def p3(self):
		return self.pts[2]

	def getPts(self):
		return self.pts

# ***** Point class stores x and y of this Point *****
class Point:
	def __init__(self, x, y):
		self.xval = x
		self.yval = y

	def x(self):
		return self.xval

	def setX(self, x):
		self.xval = x

	def y(self):
		return self.yval

	def setY(self, y):
		self.yval = y

	def __eq__(self, other):
		return self.x() == other.x() and self.y() == other.y()

# generates a "map" or list of Points for the fractal triangle pattern that will be distorted to make a mountain
def mapfractal(tri, pointMap, level, trigroups):
	# BASE CASE: level (iterator) has reached 0, stop adding points to map
	if level != 0:

		for i in range(len(tri.getPts())): # add this call's new triangle points to the map, then convert all points to indices
			if tri.getPts()[i] not in pointMap:
				pointMap.append(tri.getPts()[i])
			tri.getPts()[i] = pointMap.index(tri.getPts()[i])


		# when drawing, make sure we know to connect the points of the level 1 (smallest) triangles
		if level == 1:
			trigroups.append(tri)

		# RECURSIVE CALLS: continue drawing triangles in the top, bottom, and middle of this one
		mapfractal(Triangle( pointMap[tri.p1()], mid(pointMap[tri.p1()], pointMap[tri.p2()]), mid(pointMap[tri.p1()], pointMap[tri.p3()]) ), pointMap, level - 1, trigroups)
		mapfractal(Triangle( mid(pointMap[tri.p1()], pointMap[tri.p2()]), mid(pointMap[tri.p2()], pointMap[tri.p3()]), mid(pointMap[tri.p3()], pointMap[tri.p1()]) ), pointMap, level - 1, trigroups)
		mapfractal(Triangle( pointMap[tri.p2()], mid(pointMap[tri.p2()], pointMap[tri.p1()]), mid(pointMap[tri.p2()], pointMap[tri.p3()]) ), pointMap, level - 1, trigroups)
		mapfractal(Triangle( pointMap[tri.p3()], mid(pointMap[tri.p3()], pointMap[tri.p1()]), mid(pointMap[tri.p3()], pointMap[tri.p2()]) ), pointMap, level - 1, trigroups)

		return [pointMap, trigroups]

# ***** takes two Points and returns their midpoint *****
def mid(a, b):
	return Point((a.x() + b.x())/2, (a.y() + b.y())/2)

# ***** randomly adjusts points in the map, based on the length of the sides of the smallest triangles (bc too much distortion --> gross) *****
def bend(pointMap, sideLen):
	for pt in pointMap:
		pt.setX(pt.x() + random.randrange(-sideLen/10, sideLen/10))
		pt.setY(pt.y() + random.randrange(-sideLen/10, sideLen/10))

def color(pointMap, trigroups, t):
	for tri in trigroups:
		rand = random.randrange(50, 100)
		t.fillcolor(rand + 100, rand, rand)
		t.up()
		t.goto(pointMap[tri.p1()].x(), pointMap[tri.p1()].y())
		t.begin_fill()
		t.goto(pointMap[tri.p2()].x(), pointMap[tri.p2()].y())
		t.goto(pointMap[tri.p3()].x(), pointMap[tri.p3()].y())
		t.end_fill()

numlevels = 5
length = 700

t = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
t.speed(0)

# ptsandcolor[0] = points, ptsandcolor[1] = color groups
ptsandcolor = mapfractal(Triangle(Point(-length/2,0), Point(length/2,0), Point(0,length*0.4)), [], numlevels, [])
bend(ptsandcolor[0], length/numlevels) # length/numlevels = side length of smallest triangles
color(ptsandcolor[0], ptsandcolor[1], t)

screen.exitonclick()



