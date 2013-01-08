# Show algebra problems functions

#  print "		0: ax+b=c"
def showaxpbeqc(v,a,x,b):
  c = (v*a)+b
  print "%i%c+%i=%i (%c=%i)" % (a,x,b,c,x,v)
  o = ") %i%c+%i=%i (%c=%i)" % (a,x,b,c,x,v)
  return o

#  print "		1: ax+b=cx+d"
def showaxbeqcxd(v,a,x,b,c):
  one = (v*a)+b
  d = one - (v*c)
  o = ""
  if c < 0:
    print "%i%c+%i=%i%i%c (%c=%i)" % (a,x,b,d,c,x,x,v)
    o = ") %i%c+%i=%i%i%c (%c=%i)" % (a,x,b,d,c,x,x,v)
  elif d < 0:
    print "%i%c+%i=%i%c%i (%c=%i)" % (a,x,b,c,x,d,x,v)
    o = ") %i%c+%i=%i%c%i (%c=%i)" % (a,x,b,c,x,d,x,v)
  else:
    print "%i%c+%i=%i%c+%i (%c=%i)" % (a,x,b,c,x,d,x,v)
    o = ") %i%c+%i=%i%c+%i (%c=%i)" % (a,x,b,c,x,d,x,v)

#  print "		2: ax^2+bx-c (GCF)"
#  print "		3: area/perim of a triangle"
#  print "		4: area/perim of a quadrilateral"
#  print "		5: a(bx-c)=d"
#  print "		6: x^3-y^3"
#  print "		7: ax^2+bx-c=0"
