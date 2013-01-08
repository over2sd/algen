#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys
import getopt
import re
from random import randint

ver = "0.5"

def main(argv):
  cnt = 1
  mn = 1
  mx = 10
  vlist = "abcdefghiklmnopqrstuvwxyz"
  twoside = False
  out = ""
  lines = []
  try:
    opts, args = getopt.getopt(argv, "c:dhn:o:v:x:", ["double-sided","count=","min=","max=","vars=","outfile=","help"])
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
    elif opt in ("-o","--outfile"):
      out = arg
      try:
        o = open(out,'a')
        o.close()
      except IOError as e:
        print "Could not open %s for output: %s. Skipping." % (out,e)
  for i in range(cnt):
    part1 = randint(mn,mx) # x
    part2 = randint(mn,mx) # coefficent
    part3 = randint(mn,mx) # constant
    part4 = randint(mn,mx) # second coefficent (for double-sided)
    var = vlist[randint(0,len(vlist)-1)]
    part5 = (part1*part2)+part3
    print "%i) %i%c+%i=%i (%c=%i)" % (i+1,part2,var,part3,part5,var,part1)
    if out is not "": lines.append("\n%i) %i%c+%i=%i (%c=%i)" % (i+1,part2,var,part3,part5,var,part1))
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
  print "Usage: %s [-c|--count <#>] [-n|--min <#>] [-x|--max <#>] [-v|--vars <string>] [-o|--outfile <file>]" % sys.argv[0]
  print "-c, --count:		How many problems to generate"
  print "-n, --min:		Minimum value for variable, coefficients, and constants"
  print "-x, --max:		Maximum value for variable, coefficients, and constants"
  print "-v, --vars:		String of lowercase letters that can be used for variables (e.g., \"-v x\", \"-v abc\""
  print "-o, --outfile:		A filename where the program will append its results for easy copy/paste"
  print "-t, --types:		Type(s) of problems to generate (not implemented)"

if __name__ == "__main__":
  print "Loading %s v%s..." % (sys.argv[0],ver)
  main(sys.argv[1:])