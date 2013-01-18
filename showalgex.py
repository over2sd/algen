# Show algebra problems functions
import re
from math import (sqrt, fabs)
from random import randint

def trianglesanity(a,b,c):
  # No side may be 0
  if a == 0: a += 1
  if b == 0: b += 1
  if c == 0: c += 1
  # All sides must be positive
  a = fabs(a)
  b = fabs(b)
  c = fabs(c)
  # no side may be >= sum of the other two sides
  check = 0
  while check == 0:
    if a-c >= b: b += 1
    if b-c >= a: a += 2
    if c-b >= a: a += 1
    if c-a >= b: b += 2
    if a-b >= c: c += 1
    if b-a >= c: c += 2
    if (a < b+c and b < a+c and c < a+b): check = 1
  return (int(a),int(b),int(c))

def areafromsides(a,b,c): # assumes correct triangle dimensions, which must be true, because this function returns only the area.
  m = (a+b+c)/2.00 # magic number
  try:
    area = sqrt(m*(m-a)*(m-b)*(m-c))
    if area == 0:
      print "ARGH! %f %f %f => %f => %f" % (a,b,c,m,area)
    return area
  except ValueError as e:
    print "Oops: %s given a=%i, b=%i, c=%i (probably means this is not a triangle!)" % (e,a,b,c)
    return 0

def cleaneq(s):
  s = re.sub('\+-','-',s)
  s = re.sub('--','+',s)
  return s

#  print "		0: ax+b=c"
def showaxpbeqc(v,a,x,b):
  c = (v*a)+b
  o = ") %i%c+%i=%i (%c=%i)" % (a,x,b,c,x,v)
  return cleaneq(o)

#  print "		1: ax+b=cx+d"
def showaxbeqcxd(v,a,x,b,c):
  if c == a: # prevent equation tautology (6x-3=6x-3)
    d = b
    b = a
    a = d
#    print "\nflipped a and b"
  one = (v*a)+b
  d = one - (v*c)
  o = ""
  if c < 0: # reverse order of second half if variable part is negative
    o = ") %i%c+%i=%i+%i%c (%c=%i)" % (a,x,b,d,c,x,x,v)
  else:
    o = ") %i%c+%i=%i%c+%i (%c=%i)" % (a,x,b,c,x,d,x,v)
  return cleaneq(o)

#  print "		2: y=ax^2+bx-c (or GCF)"
def showgcfax2pbxmc(v,x,d,e,f,g):
  # for (dx+e)(fx+g)
  h = d*f
  i = d*g
  j = e*f
  k = e*g
  a = h
  b = i+j
  c = k
  t = (a*(v*v))+(b*v)-c
  o = ") %i%c^2+%i%c-%i (%i%c+%i)(%i%c-%i) (f(%i)=%i)" % (a,x,b,x,c,d,x,e,f,x,g,v,t)
  return cleaneq(o)

#  print "		3/8: area/perim of a triangle"
def showtriangle(u,m,n,b=0):
  a = 1
  c = 1
  o = ") "
  if b == 0: # if o != 0, generate triangle that is not right
    (m,b,n) = trianglesanity(m,b,n)
    if (n>m): # Shouldn't happen, but let's fix it automagically.
      z = m
      m = n
      n = z
    if (n==m): m += 1 # prevents a=0
    a = (m*m)-(n*n)
    b = 2*m*n
    c = (m*m)+(n*n)
    area = 0.5*(a*b)
    p = a+b+c
    h = ((a*a)+(b*b))/c
    #  print "Given %i and %i: a=%i b=%i c=%i=%i" % (m,n,a,b,c,h)
    o += "A right triangle has legs x %s and %i%s and a hypotenuse of %i%s. Find the area and perimeter. (x=%i%s, a=%.4f%s^2, p=%.4f%s)" % (u,b,u,c,u,a,u,area,u,p,u)
  else:
    (m,b,n) = trianglesanity(m,b,n)
    area = areafromsides(b,m,n)
    a = m
    c = n
    h = 2*area/b
    p = a+b+c
    o += "A triangle has sides of %i%s, %i%s, and %i%s. The height of the triangle, measured with the second side (%i%s) as the base, is %.6f%s. Find the perimeter and area. (p=%.3f%s, a=%.3f%s^2)" % (a,u,b,u,c,u,b,u,h,u,p,u,area,u)
  return cleaneq(o)

#  print "		4: area/perim of a parallelogram"
def showpara(b,s,d,u): # base, side, diagonal, unit string
  (b,s,d) = trianglesanity(b,s,d)
  area = 2*(areafromsides(b,s,d))
  h = area/b
  p = 2*b+2*s
  o = ") A parallelogram has a height of %.6f%s, a base of %i%s, and an adjacent side of %i%s. Find the area and perimeter. (A=%.3f%s^2, P=%i%s)" % (h,u,b,u,s,u,area,u,p,u)
  return o

#  print "		5: a(bx-c)=d"
def showabxmc(v,a,b,x,c):
  e = a*(b*v)
  f = a*c
  d = e-f
  o = ") %i(%i%c-%i)=%i (%c=%i)" % (a,b,x,c,d,x,v)
  return cleaneq(o)

#  print "		6: x^3-y^3"
def showx3my3(v,x,a):
  if a <= 0:
    a = int(fabs(a)+1)
  y3 = a*a*a
  b = a*a
  c = (v*v*v) - y3
  o = ") %c^3-%i (%c-%i)(%c^2+%i%c+%i) (f(%i)=%i)" % (x,y3,x,a,x,a,x,b,v,c)
  return cleaneq(o)

def showsimpineq(v,a,x,b):
  i = '='
  if (a == 0): a += 1
  c = (v*a)+b
  d = randint(0,3)
  ilist = ["<","<=",">",">="]
  i = ilist[d]
  e = 0
  if (a < 0):
    e = 2
  i2 = ilist[(d+e) % 4]
  o = ") %i%c+%i%s%i (%c%s%i)" % (a,x,b,i2,c,x,i,v)
  return cleaneq(o)

def saywordprob(t,x,v,a,b,c='',d='',e=''):
  o = ""
  #if t == '0':
  names = ["Hannah","Emily","Sarah","Madison","Brianna","Kaylee","Kaitlyn","Hailey","Alexis",
    "Elizabeth","Michael","Jacob","Matthew","Nicholas","Christopher","Joseph","Zachary",
    "Joshua","Andrew","William"]
  txt1 = ["has enough money for %i %s with","will have enough money to have a party after saving allowance money for %i weeks, along with","wrote %i more lines of video game code than"]
  txt2 = ["ponies","super flyers","monkeys","concert tickets"]
  txt3 = ["left over.","already saved."]
  txt4 = ["What is the cost for one?","How much is the weekly allowance?"]
  return o

def unittest(a = 0, b = 0, c = 0):
  print showsimpineq(a,b,'x',c)
  '''
  if a == 0 and a == b and a == c:
    for a in range(1,10):
      for b in range(1,10):
        for c in range(1,10):
          (d,e,f) = trianglesanity(a,b,c)
          print "Triangle: %i %i %i from given %i %i %i for change of %i %i %i" % (d,e,f,a,b,c,d-a,e-b,f-c)
  else:
    print "%i %i %i " % (a,b,c),
    (d,e,f) = trianglesanity(a,b,c)
    print "Triangle: %i %i %i from Given %i %i %i for change of %i %i %i" % (d,e,f,a,b,c,d-a,e-b,f-c)
  '''
  return

