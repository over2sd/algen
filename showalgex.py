#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

# Show algebra problems functions
import re
from math import (sqrt, fabs, fmod)
from random import randint
from fractions import Fraction
from decimal import Decimal

def fractionize(n,x,d,mixedvar=0):
  if d == 0: return "div/0! undefined"
  if n == 0: return "0"
  f = ""
  fr = Fraction (n,d)
  n = fr.numerator
  d = fr.denominator
  if n % d == 0:
    f = "%i%s" % (n/d,x)
  elif abs(n) > d and (len(x) == 0 or mixedvar):
      sign = n/abs(n)
      a = n * sign
      (w,r) = divmod(a,d)
      f = "%i %i%s/%i" % (w*sign,r,x,d)
  else:
    f = "%i%s/%i" % (n,x,d)
  return f

def trimfloat(f,p=1):
  o = "%f" % f
  mn = 3
  if '.' not in o: return o
  else: mn = o.find('.') + 2
  if mn < p + 2 or mn < 3: mn = p + 2
  while o[-1] == '0' and len(o) > mn: # len(0.0) = 3
    o = o[:-1]
  return o

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
  o = "%i%c+%i=%i" % (a,x,b,c)
  k = "(%c=%i)" % (x,v)
  return (cleaneq(o),cleaneq(k))

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
    o = "%i%c+%i=%i+%i%c" % (a,x,b,d,c,x)
  else:
    o = "%i%c+%i=%i%c+%i" % (a,x,b,c,x,d)
  k = "(%c=%i)" %  (x,v)
  return (cleaneq(o),cleaneq(k))

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
  o = "%i%c^2+%i%c-%i" % (a,x,b,x,c)
  k = "(%i%c+%i)(%i%c-%i) (f(%i)=%i)" % (d,x,e,f,x,g,v,t)
  return (cleaneq(o),cleaneq(k))

#  print "		3/8: area/perim of a triangle"
def showtriangle(u,m,n,b=0,integers=0,t=0):
  a = 1
  c = 1
  h = 1
  o = ""
  z = ""
  k = ""
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
    o += "A right triangle has legs x %s and %i%s and a hypotenuse of %i%s. Find the area and perimeter." % (u,b,u,c,u)
    k = "(x=%i%s, a=%s%s^2, p=%s%s)" % (a,u,trimfloat(area),u,trimfloat(p),u)
  else:
    (m,b,n) = trianglesanity(m,b,n)
    if integers: (m,n,b,h,z) = makewholetri(m,b,n,t)
    print h,
    area = areafromsides(b,m,n)
    a = m
    c = n
    h = 2*area/b
    p = a+b+c
    y = "%.3f%s" % (a,u)
    if a == int(a) or u == "px":
      y = "%i%s" % (a,u)
    elif u == "AU": # a bit of fun with enormous distances
      y = "%f%s" % (a,u)
    bh = "%.3f%s" % (h,u)
    if h == int(h) or u == "px":
      bh = "%i%s" % (h,u)
    elif u == "AU":
      bh = "%f%s" % (h,u)
    w = "%i%s" % (b,u) if (b == int(b) or u == "px") else "%.3f%s" % (b,u)
    area = "%i%s" % (area,u) if u == "px" or area == int(area) else "%.3f%s" % (area,u)
    p = "%i%s" % (p,u) if u == "px" or p == int(p) else "%.3f%s" % (p,u)
    o += "A%s triangle has sides of %s, %s, and %i%s. The height of the triangle, measured with the second side (%s) as the base, is %s. Find the perimeter and area." % (z,y,w,c,u,w,bh)
    k = "(p=%s, a=%s^2)" % (p,area)
  return (cleaneq(o),cleaneq(k))

def makewholetri(a,b,c,bigangle):
  s = ""
  if a < 2: a = 2
  if b < 2: b = 2
  if c < 2: c = 2
  if (a == b and b == c):
    a += 1; b += 2; c += 3
  hc,a,b = sorted([a,b,c]) # line 133
  d = sqrt((a*a)-(hc*hc))
  e = sqrt((b*b)-(hc*hc))
  f = sqrt((b*b)+(a*a))
  if bigangle in [0,1]: # [any angle okay, acute]
    c = d+e
    if c > f: c = f # any bigger, and it's obtuse at the apex, so make it right, and it'll be rounded down to acute
  else: # obtuse
    c = e - d
    if c <= 1 or (c < f and (e+d < f)): c = f+1
  if c != int(c): # note to self: don't deindent: doing more here than flooring c
    c = int(c)
    if bigangle == 2 and e > c: d = e - c # obtuse
    else: d = c - e # acute/any
    a = sqrt((d*d)+(hc*hc))
#  print (c*c,b*b,a*a),
  if c == sqrt((a*a)+(b*b)) or b == sqrt((a*a)+(c*c)): s = " right" #  or a == sqrt((b*b)+(c*c)) # removed because it shouldn't ever be true (see line 133)
  elif ((c*c < ((b*b)-(a*a))) or (c*c > ((b*b)+(a*a)))): s = "n obtuse"
  else: s = "n acute"
#  print "=> h: %i ss: %.4f and %i, b: %i. (%s)" % (hc,a,b,c,s)
  return (a,b,c,hc,s)

#  print "		4: area/perim of a parallelogram"
def showpara(b,s,d,u,integers=0): # base, side, diagonal, unit string, whole altitude? (opt)
  (b,s,d) = trianglesanity(b,s,d)
  area = 2*(areafromsides(b,s,d))
  h = area/b
  if u == "px": u = "cm" # no pixels for this one
  if integers and h != int(h):
    h = int(h+0.5)
    area = h*b
  h = "%i%u" % (h,u) if h == int(h) else "%.6f%s" % (h,u)
  p = 2*b+2*s
  o = "A parallelogram has a height of %s, a base of %i%s, and an adjacent side of %i%s. Find the area and perimeter." % (h,b,u,s,u)
  k = "(A=%s%s^2, P=%i%s)" % (trimfloat(area),u,p,u)
  return (o,k)

#  print "		5: a(bx-c)=d"
def showabxmc(v,a,b,x,c):
  e = a*(b*v)
  f = a*c
  d = e-f
  o = "%i(%i%c-%i)=%i" % (a,b,x,c,d)
  k = "(%c=%i)" % (x,v)
  return (cleaneq(o),k)

#  print "		6: x^3-y^3"
def showx3my3(v,x,a):
  if a <= 0:
    a = int(fabs(a)+1)
  y3 = a*a*a
  b = a*a
  c = (v*v*v) - y3
  o = "%c^3-%i" % (x,y3)
  k = "(%c-%i)(%c^2+%i%c+%i) (f(%i)=%i)" % (x,a,x,a,x,b,v,c)
  return (cleaneq(o),cleaneq(k))

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
  o = "%i%c+%i%s%i" % (a,x,b,i2,c)
  k = "(%c%s%i)" % (x,i,v)
  return (cleaneq(o),k)

def showfracgcf(a, b,allow1):
  spin = 0
#  x = "%i,%i" % (a,b)
#  print x,
  if a < 0: a *= -1
  if b < 0: b *= -1
  if a == 0:
    a = 6
  else:
    a += 5
  if b == 0: b = a
  if a == 1: a = 2
  if b == 1: b = 2 # 1 produces unreducible fractions
  b,a = sorted([a,b]) # a should be larger than b
  sub = (a + b) / 2
  if sub in [a,b]: sub /= 2
  if sub > a: sub = a - 1
  ns = 2
  if sub > 2:
    ns = randint(2,sub)
  nb = a - ns
  db = 0
  ds = 1
  if nb < 0: nb *= -1
  if nb == 0: nb = 1
  while db < nb or db == 0:
    ds = 1
    if sub > 2:
      ds = randint(1,sub - 1)
    db = a - ds
    spin += 1
    if spin > 100: db = nb + 1
  n = nb * b
  d = db * b
  if n == d and n in [4,9,16,25,36,49,64,81,100,121,144,169,196,225]: n = sqrt(d)
  elif n == d and n%2 == 0: d = n + 2
  elif n == d and allow1 == 0 and n > 6:
    n -= randint(2,n - 3)
  elif n == d and allow1 == 0: n = randint(1,30); d = n * randint(2,3)
  b = euclid_gcf(d,n)
  nb = n / b
  db = d / b
  o = "%i/%i" % (n,d)
  k = "(%i/%i GCF=%i)" % (nb,db,b)
  if nb != nb+0.00 or db != db+0.00: return "error %s" % o
  return (o,k)

def euclid_gcf(a,b):
  while b != 0:
    a,b = b,a%b
  return a

def showaxpbeqcfrac(v,a1,a2,x,b,mixedco=0):
  if a2 == 0: a2 = 7.00
  """
  if a1 < 0: a1 *= -1
  if a2 < 0: a2 *= -1
  a1 = int(a1)
  a2 = int(a2)
  a1 += 0.00 if a1 > 0 else 2.00
  a2 += 0.00 if a2 > 0 else 7.00
  """
  b = int(b)
  fr = fractionize(a1,x,a2,mixedco)
  ax = "%s" % fr
  c = v*a1
  c += b*a2
  c = fractionize(c,"",a2)
  o = "%s+%i=%s" % (ax,b,c)
  k = "(%c=%i)" % (x,v)
  return (cleaneq(o),k)

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
  el = {}
  er = []
  for a in range(-5,10):
    for b in range(-5,10):
#      for c in range(-2,15):
#        for d in ["x",""]:
      e = fractionize(a,"xy",b)
      print e
      if "ERR" in e:
        er.append((a,b,c))
        el[str(a)] = []
#          print showaxpbeqcfrac(7,a,b,'x',c)
#          print "Triangle: %i %i %i from given %i %i %i (%s)" % (e,f,g,a,b,c,i)
  print "--------"
  for x in er:
    (a,b,c) = x
    el[str(a)].append((b,c))
  for x in sorted(el.keys()):
    print "\n%s: " % (x),
    for y in el[x]:
      (b,c) = y
      print "%s/%s" % (b,c),
  return

if __name__ == "__main__":
  print "\nThis file is not meant to be called by the user. Please use algen.py instead."
  exit(-1)
