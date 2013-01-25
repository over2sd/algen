#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys
import getopt
from random import randint
from math import (fabs,fmod)

import showalgex

ver = "0.9.07"

def main(argv):
  debugutest = 0
  cnt = 1
  mn = 1
  mx = 10
  vlist = "abcdefghikmnpqrstuvwxyz"
  out = ""
  lines = []
  boring = [-1,0,1]
  gcfone = 0
  tlist = "0123456789a"
  units = ["mm","cm","in","ft","m","yds","km","mi","AU","px"]
  u = 0
  unit = "spans"
  integers = 0
  keysep = 0
  key = []
  try:
    opts, args = getopt.getopt(argv, "ac:hkn:o:t:u:v:x:01", ["count=","min=","max=","vars=","outfile=","help","allowzero","types=","unit=","test","allowone","wholealt","keyafter"])
  except getopt.error as err:
    print "Error: %s\n" % err
    usage()
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-h","--help"):
      usage()
      sys.exit(0)
    elif opt in ("-c","--count"):
      if isnum(arg):
        cnt = int(arg)
      else:
        print "Argument is not a valid number. Ignoring %s %s.\n" % (opt,arg)
    elif opt in ("-x","--max"):
      if isnum(arg):
        mx = int(arg)
      else:
        print "Argument is not a valid number. Ignoring %s %s.\n" % (opt,arg)
    elif opt in ("-t","--types"):
      # need sanity check?
      tlist = arg
    elif opt in ("-u","--unit"):
      # need sanity check?
      unit = arg
      u = -1
    elif opt in ("-n","--min"):
      if isnum(arg):
        mn = int(arg)
      else:
        print "Argument is not a valid number. Ignoring %s %s.\n" % (opt,arg)
    elif opt in ("-v","--vars"):
      arg = loweronly(arg)
      if len(arg) > 0:
        vlist = arg
      else:
        print "Argument is not valid. Ignoring %s %s and using \"%s\" for possible variables.\n" % (opt,arg,vlist)
    elif opt in ("-0","--allowzero"):
      boring = []
    elif opt in ("-k","--keyafter"):
      keysep = 1
    elif opt in ("-a","--wholealt"):
      integers = 1
    elif opt in ("-1","--allowone"):
      gcfone = 1
    elif opt == "--test":
      debugutest = 1
    elif opt in ("-o","--outfile"):
      out = arg
      try:
        f = open(out,'a')
        f.close()
      except IOError as e:
        print "Could not open %s for output: %s. Skipping." % (out,e)
  if debugutest == 1:
    for i in range(cnt):
      a = randint(mn,mx)
      b = randint(mn,mx)
      c = randint(mn,mx)
      showalgex.unittest(a,b,c)
    sys.exit(0)
  if mx <= 1 and mn >=-1: boring = [] # only you can prevent infinite loops
  exlist = []
  while len(exlist) < cnt: # until we have at least as many listed types as we want exercises...
    exlist += tlist # add on exercise types from list of desired types
  exlist = exlist[:cnt] # trim to desired length
  i = 0
  for probtype in exlist:
    part1 = randint(mn,mx) # x
    part2 = randint(mn,mx) # a
    part3 = randint(mn,mx) # b
    part4 = randint(mn,mx) # c/y
    part5 = randint(mn,mx) # d
    while part1 in boring: part1 = randint(mn,mx) # x
    while part2 in boring: part2 = randint(mn,mx) # a
    while part3 in boring: part3 = randint(mn,mx) # b
    while part4 in boring: part4 = randint(mn,mx) # c/y
    while part5 in boring: part5 = randint(mn,mx) # d
    var = vlist[randint(0,len(vlist)-1)]
    i += 1
    o = ""
    if probtype == '0': (o,a) = showalgex.showaxpbeqc(part1,part2,var,part3)
    elif probtype == '1': (o,a) = showalgex.showaxbeqcxd(part1,part2,var,part3,part4)
    elif probtype == '2': (o,a) = showalgex.showgcfax2pbxmc(part1,var,part2,part3,part4,part5)
    elif probtype in '37':
      if u >= 0:
        u = fabs(randint(mn,mx))
        u = u % len(units)
        unit = units[int(u)]
      if part1 < 1: fabs(part1) # must be positive
      if part2 < 1: fabs(part2) # must be positive
      if part1 == part2: part1 += 1 # must not be equal
      if probtype == '3':
        part3 = 0
      else:
        part3 = fabs(part3)
      (o,a) = showalgex.showtriangle(unit,part1,part2,part3,integers,0)

    elif probtype == '4':
        if u >= 0:
          u = fabs(randint(mn,mx))
          u = u % len(units)
          unit = units[int(u)]
        (o,a) = showalgex.showpara(part1,part2,part3,unit,integers)
    elif probtype == '5': (o,a) = showalgex.showabxmc(part1,part2,part3,var,part4)
    elif probtype == '6': (o,a) = showalgex.showx3my3(part1,var,part2)
    elif probtype == '8': (o,a) = showalgex.showsimpineq(part1,part2,var,part3)
    elif probtype == '9': (o,a) = showalgex.showfracgcf(part1,part2,gcfone)
    elif probtype == 'a': (o,a) = showalgex.showaxpbeqcfrac(part1,part2,part3,var,part4)
    if keysep:
      key.append("%i) %s" % (i,a))
    else: o = "%s %s" % (o,a)
    print "%i) %s" % (i,o)
    if out is not "": lines.append("\n%i) %s" % o)
  for l in key:
    print "a%s" % l
  if out is not "":
    with open(out,'a') as f:
      for l in lines:
        f.write(l)
      if len(key) > 0: f.write("\nAnswers:")
      for l in key:
        f.write("\n%s" % l)
      f.write("\n")
      f.close()

def loweronly(s):
  o = ''
  for c in s:
    if c in "qwertyuiopasdfghjklzxcvbnm": o += c
  return o

def isnum(x):
  try:
    float(x)
    return True
  except ValueError:
    return False
  except TypeError:
    return False

def usage():
  print "Usage: %s [option value]" % sys.argv[0]
  print "-c <#>, --count <#>:		How many exercises to generate"
  print "-n <#>, --min <#>:		Minimum value for variable, coefficients,\n\tand constants"
  print "-x <#>, --max <#>:		Maximum value for variable, coefficients,\n\tand constants"
  print "-v <char|string>, --vars <char|string>:		String of lowercase letters\n\tthat can be used for variables"
  print "	Examples: \"-v x\", \"-v abc\""
  print "-o <file>, --outfile <file>:		A filename where the program will\n\tappend its results for easy copy/paste"
  print "-t <types>, --types <types>:		Type(s) of exercises to generate:"
  print "		0: ax+b=c"
  print "		1: ax+b=cx+d"
  print "		2: ax^2+bx-c (=d or GCF)"
  print "		3: area/perim of a right triangle"
  print "		4: area/perim of a parallelogram"
  print "		5: a(bx-c)=d"
  print "		6: x^3-y^3"
  print "		7: area/perim of a triangle"
  print "		8: simple inequality (e.g. ax+b>c)"
  print "		9: Reducing/GCF of fractions"
  print "	Examples: \"-t 138af\" \"-t 2\""
  print "-0, --allowzero:		Allow value of x, a, b, c... to be\n\tboring (0, 1, or -1)"
  unit = ["parsecs","furlongs","picas","pt","leagues","rods","knots","mil","nm"]
  unit = unit[randint(0,len(unit)-1)]
  print "-u <string>, --unit <string>:		Text to put after measurements\n\t(e.g., %s)" % unit
  print "-a, --wholealt:		Do not allow decimal points in altitudes"
  print "-k, --keyafter:		Give key after all exercises (default after each)"

if __name__ == "__main__":
  print "\nLoading Algebra Exercise Generator v%s..." % (ver)
  main(sys.argv[1:])