# Show algebra problems functions

#  print "		0: ax+b=c"
def showaxpbeqc(v,a,x,b):
  c = (v*a)+b
  o = ") %i%c+%i=%i (%c=%i)" % (a,x,b,c,x,v)
  return o

#  print "		1: ax+b=cx+d"
def showaxbeqcxd(v,a,x,b,c):
  one = (v*a)+b
  d = one - (v*c)
  o = ""
  if c < 0: #TODO: Clean this up so -- becomes +, etc.
    o = ") %i%c+%i=%i%i%c (%c=%i)" % (a,x,b,d,c,x,x,v)
  elif d < 0:
    o = ") %i%c+%i=%i%c%i (%c=%i)" % (a,x,b,c,x,d,x,v)
  else:
    o = ") %i%c+%i=%i%c+%i (%c=%i)" % (a,x,b,c,x,d,x,v)
  return o

#  print "		2: ax^2+bx-c (GCF)"
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
  return o

#  print "		3: area/perim of a triangle"
def showtriangle(m,n):
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
  o = ") A right triangle has legs x cm and %icm and a hypotenuse of %icm. Find the area and perimeter. (x=%icm, a=%icm^2, p=%icm)" % (b,c,a,area,p)
  return o

#  print "		4: area/perim of a quadrilateral"

#  print "		5: a(bx-c)=d"
def showabxmc(v,a,b,x,c):
  e = a*(b*v)
  f = a*c
  d = e-f
  o = ") %i(%i%c-%i)=%i (%c=%i)" % (a,b,x,c,d,x,v)
  return o

#  print "		6: x^3-y^3"
def showx3my3(v,x,a):
  pass

#  print "		7: ax^2+bx-c=0"
