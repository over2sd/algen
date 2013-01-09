#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys
import getopt
import re
from random import randint

import showalgex

ver = "0.7"

def main(argv):
  cnt = 1
  mn = 1
  mx = 10
  vlist = "abcdefghikmnopqrstuvwxyz"
  twoside = False
  out = ""
  lines = []
  boring = [-1,0,1]
  tlist = "01235"
  try:
    opts, args = getopt.getopt(argv, "c:dhn:o:v:x:0t:", ["double-sided","count=","min=","max=","vars=","outfile=","help","allowzero","types="])
  except getopt.error as err:
    print "Error: %s\n" % err
    usage()
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-d","--double-sided"): twoside = True
    elif opt in ("-h","--help"):
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
    elif opt in ("-o","--outfile"):
      out = arg
      try:
        o = open(out,'a')
        o.close()
      except IOError as e:
        print "Could not open %s for output: %s. Skipping." % (out,e)
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
    if probtype == '0': o = showalgex.showaxpbeqc(part1,part2,var,part3)
    elif probtype == '1': o = showalgex.showaxbeqcxd(part1,part2,var,part3,part4)
    elif probtype == '2': o = showalgex.showgcfax2pbxmc(part1,var,part2,part3,part4,part5)
    elif probtype == '3':
      if part1 < 1: part1 *= -1 # must be positive
      if part2 < 1: part2 *= -1 # must be positive
      if part1 == part2: part1 += 1 # must not be equal
      o = showalgex.showtriangle(part1,part2)
    elif probtype == '5': o = showalgex.showabxmc(part1,part2,part3,var,part4)
    print "%i%s" % (i,o)
    if out is not "": lines.append("\n%s" % o)
  if out is not "":
    with open(out,'a') as f:
      for l in lines:
        f.write(l)
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
  print "-n <#>, --min <#>:		Minimum value for variable, coefficients, and constants"
  print "-x <#>, --max <#>:		Maximum value for variable, coefficients, and constants"
  print "-v <char|string>, --vars <char|string>:		String of lowercase letters that can be used for variables"
  print "	Examples: \"-v x\", \"-v abc\""
  print "-o <file>, --outfile <file>:		A filename where the program will append its results for easy copy/paste"
  print "-t <types>, --types <types>:		Type(s) of exercises to generate:"
  print "		0: ax+b=c"
  print "		1: ax+b=cx+d"
  print "		2: ax^2+bx-c (GCF)"
  print "		3: area/perim of a right triangle"
#  print "		4: area/perim of a quadrilateral"
  print "		5: a(bx-c)=d"
#  print "		6: x^3-y^3"
#  print "		7: ax^2+bx-c=0"
  print "	Examples: \"-t 138af\" \"-t 2\""
  print "-0, --allowzero:		Allow value of x, a, b, c... to be boring (0, 1, or -1)"

if __name__ == "__main__":
  print "Loading Algebra Exercise Generator v%s..." % (sys.argv[0],ver)
  main(sys.argv[1:])