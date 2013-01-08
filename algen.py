#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys
import getopt
import re
from random import randint

import showalgex

ver = "0.6"

def main(argv):
  cnt = 1
  mn = 1
  mx = 10
  vlist = "abcdefghiklmnopqrstuvwxyz"
  twoside = False
  out = ""
  lines = []
  boring = [-1,0,1]
  try:
    opts, args = getopt.getopt(argv, "c:dhn:o:v:x:0", ["double-sided","count=","min=","max=","vars=","outfile=","help","allowzero"])
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
  for i in range(cnt):
    part1 = randint(mn,mx) # x
    part2 = randint(mn,mx) # a
    part3 = randint(mn,mx) # b
    part4 = randint(mn,mx) # c/y
    while part1 in boring: part1 = randint(mn,mx) # x
    while part2 in boring: part2 = randint(mn,mx) # a
    while part3 in boring: part3 = randint(mn,mx) # b
    while part4 in boring: part4 = randint(mn,mx) # c/y
    var = vlist[randint(0,len(vlist)-1)]
    print "%i) " % (i+1),
    probtype = '1'
    o = ""
    if probtype == '0': o = showalgex.showaxpbeqc(part1,part2,var,part3)
    elif probtype == '1': o = showalgex.showaxbeqcxd(part1,part2,var,part3,part4)
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
  print "-c <#>, --count #:		How many problems to generate"
  print "-n <#>, --min #:		Minimum value for variable, coefficients, and constants"
  print "-x <#>, --max:		Maximum value for variable, coefficients, and constants"
  print "-v <#>, --vars:		String of lowercase letters that can be used for variables (e.g., \"-v x\", \"-v abc\")"
  print "-o <file>, --outfile:		A filename where the program will append its results for easy copy/paste"
#  print "-t <types>, --types:		Type(s) of problems to generate:"
#  print "		0: ax+b=c"
#  print "		1: ax+b=cx+d"
#  print "		2: ax^2+bx-c (GCF)"
#  print "		3: area/perim of a triangle"
#  print "		4: area/perim of a quadrilateral"
#  print "		5: a(bx-c)=d"
#  print "		6: x^3-y^3"
#  print "		7: ax^2+bx-c=0"
#  print "	Examples: \"-t 138af\" \"-t 2\""
  print "-0, --allowzero:		Allow value of x, a, b, c... to be boring (0, 1, or -1)"

if __name__ == "__main__":
  print "Loading %s v%s..." % (sys.argv[0],ver)
  main(sys.argv[1:])