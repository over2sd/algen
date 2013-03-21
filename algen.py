#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys
import getopt
from random import randint
from math import (fabs,fmod)
import re

import showalgex

ver = "0.9.20"

def main(argv):
  debugutest = 0
  cnt = 1
  mn = 1
  mx = 10
  vlist = "abcdefghjkmnprstuvwxyz"
  out = ""
  lines = []
  boring = [-1,0,1]
  gcfone = 0
  tlist = "0123456789abcd"
  nogame = "234679ab"
  units = ["mm","cm","in","ft","m","yds","km","mi","AU","px"]
  u = 0
  unit = "spans"
  integers = 0
  keysep = 0
  key = []
  mixedco = 0
  fractions = 0
  wordy = 0
  nodupe = 0
  rord = 0
  drill = 0
  var = ''
  game = 0
  crypt = {}
  quote = "The quick brown fox jumps over the lazy dog."
  mindiff = 3
  xvals = []
  try:
    opts, args = getopt.getopt(argv, "ac:d:fg:hkmn:o:q:rs:t:u:v:w:x:01", ["count=","min=","max=","vars=","outfile=","help","allowzero","types=","unit=","test","allowone","wholealt","keyafter","fractco","mixedvar","wordy","drill=","rand","game=","quote=","spread="])
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
    elif opt in ("-q","--quote"):
      # need sanity check?
      quote = arg
    elif opt in ("-n","--min"):
      if isnum(arg):
        mn = int(arg)
      else:
        print "Argument is not a valid number. Ignoring %s %s.\n" % (opt,arg)
    elif opt in ("-g","--game"):
      if isnum(arg):
        game = int(arg)
        keysep = 1
      else:
        print "Argument is not a valid number. Ignoring %s %s.\n" % (opt,arg)
    elif opt in ("-w","--wordy"):
      if isnum(arg):
        wordy = int(arg)
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
      nodupe = 1
    elif opt in ("-f","--fractco"):
      fractions = 1
    elif opt in ("-m","--mixedvar"):
      mixedco = 1
    elif opt == "--test":
      debugutest = 1
    elif opt in ("-r","--rand"):
      rord = 1
    elif opt in ("-s","--spread"):
      if isnum(arg):
        mindiff = int(arg)
      else:
        print "Argument is not a valid number. Ignoring %s %s.\n" % (opt,arg)
    elif opt in ("-d","--drill"):
      drill = 1
      tlist = arg if len(arg) == 1 else 0
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
  i = 0
  if drill:
    drillvar = ''
    if not isnum(tlist): tlist = tlist[0]
    if int(tlist) in [2,3,4]:
      drillvar = var if len(var) > 0 else vlist
    if cnt < 1: cnt = 1
    showalgex.showtabledrill(cnt,mx,drillvar,nodupe,rord,keysep,tlist)
    sys.exit(0)
  if (game == 1):
    letters = countLetters(quote)
    numlet = 26 if (nodupe == 0) else letters['total']
    del letters['total']
    cnt = numlet # must have a problem for each letter
    mindiff = cnt + 1 # must ALL be different
    mx = mx if (mx > mindiff + mn + 3) else mindiff + 3 if (mn < 2) else mn + mindiff # must therefore have at least mindiff spread
    vlist = "ABCDeFGHIJKLMNoPQRSTUVWXYZ" if (numlet == 26) else ''.join(letters.keys()).upper()
    vlist = re.sub('E','e',vlist)
    vlist = re.sub('O','o',vlist)
  exlist = []
  spin = 1000
  while len(exlist) < cnt and spin > 0: # until we have at least as many listed types as we want exercises...
    exlist += tlist # add on exercise types from list of desired types
    for x in reversed(range(len(exlist)-1)):
      if exlist[x] in nogame:
#        print exlist[x],
        del exlist[x]
    spin -= 1
  exlist = exlist[:cnt] # trim to desired length
  part1 = 1

  for probtype in exlist:
    part1 = randint(mn,mx) # x
    part2 = randint(mn,mx) # a
    part3 = randint(mn,mx) # b
    part4 = randint(mn,mx) # c/y
    part5 = randint(mn,mx) # d
    part6 = randint(mn,mx) # denominator
    spin = 1000
    while part1 in boring or part1 in xvals and spin:
      part1 = randint(mn,mx) # x
      spin -= 1
      if spin < 10: mx += 1 # expand possibilities when pressed
    while part2 in boring: part2 = randint(mn,mx) # a
    while part3 in boring: part3 = randint(mn,mx) # b
    while part4 in boring: part4 = randint(mn,mx) # c/y
    while part5 in boring: part5 = randint(mn,mx) # d
    while part6 in boring or part6 == part2: part6 = randint(mn,mx) # denominator
    var = vlist[randint(0,len(vlist)-1)] if (game != 1) else vlist[0]
    if (game == 1):
      vlist = vlist.replace(var,'')
    i += 1
    o = ""
    denom = part6 if fractions else 1
    if probtype == '0': (o,a) = showalgex.showaxpbeqc(part1,part2,var,part3,denom,mixedco)
    elif probtype == '1': (o,a) = showalgex.showaxbeqcxd(part1,part2,var,part3,denom,mixedco)
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
    elif probtype == '8': (o,a) = showalgex.showsimpineq(part1,part2,var,part3,denom,mixedco)
    elif probtype == '9': (o,a) = showalgex.showfracgcf(part1,part2,gcfone)
    elif probtype == 'a': (o,a) = showalgex.showmd3d(part1,part2,part3,1)
    elif probtype == 'b': (o,a) = showalgex.showunitrate(part1,part2,part3,part4,part5,wordy)
    elif probtype in ['c','d']:
      if probtype == 'c': part2 = 0
      if part1 == 0: part1 = randint(2,abs(mx)+3)
      (o,a) = showalgex.showsquareex(part1,var,part2)
    if keysep:
      key.append("%i) %s" % (i,a))
    else: o = "%s %s" % (o,a)
    print "%i) %s" % (i,o)
    if out is not "": lines.append("\n%i) %s" % o)
    if (game==1):
      crypt[var] = part1
    xvals.append(part1)
    xvals = xvals[:mindiff]
  blanks = []
  codes = []
  for x in quote:
    if (x==' '):
      blanks.append("   ")
      codes.append("   ")
      continue
    try:
      codes.append("%2i " % (crypt[x.upper()]))
      blanks.append("__ ")
    except KeyError:
      try:
        codes.append("%2i " % (crypt[x.lower()]))
        blanks.append("__ ")
      except KeyError:
        codes.append(x) # etc...
        blanks.append(x)
  print "%s\n%s" % (''.join(blanks),''.join(codes))
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

def countLetters(string):
  letters = {}
  for let in string:
    if let.isalpha():
      letters[let.upper()] = letters.get(let.upper(),0) + 1
  letters["total"] = len(letters)
  return letters

def usage():
  print "Usage: %s [option value]" % sys.argv[0]
  print "-c <#>, --count <#>:		How many exercises to generate"
  print "-n <#>, --min <#>:		Minimum value for variable, coefficients,\n\tand constants"
  print "-x <#>, --max <#>:		Maximum value for variable, coefficients,\n\tand constants; depth of times table"
  print "-v <char|string>, --vars <char|string>:		String of lowercase letters\n\tthat can be used for variables"
  print "	Examples: \"-v x\", \"-v abc\""
  print "-o <file>, --outfile <file>:		A filename where the program will\n\tappend its results for easy copy/paste"
  print "-0, --allowzero:		Allow value of x, a, b, c... to be\n\tboring (0, 1, or -1)"
  print "-1, --allowone:		Allow GCF of 1 (irreducible fraction); in drill modes, avoid duplicates; in game mode, produce just enough problems"
  unit = ["parsecs","furlongs","picas","pt","leagues","rods","knots","mil","nm"]
  unit = unit[randint(0,len(unit)-1)]
  print "-u <string>, --unit <string>:		Text to put after measurements\n\t(e.g., %s)" % unit
  print "-a, --wholealt:		Do not allow decimal points in altitudes"
  print "-k, --keyafter:		Give key after all exercises (default after each)"
  print "-f, --fractco:		Allow fractional coefficients"
  print "-m, --mixedvar:		Convert improper fractional coefficents (ax/b) to mixed numbers (a bx/c) for added challenge"
  print "-w <#>, --wordy <#>:		Make word problems, where possible. (-1:no; 0:random(default); 1:yes)"
  print "-r, --rand:	In drill modes, randomize exercise order"
  print "-s <#>, --spread <#>:	Minimum spread of identical x values (default 3)"
  print "-d <type>, --drill <type>:	Times Table Drill (with -cxkv1r)"
  print "		0 (default): multiplication (a*b= )"
  print "		1: division (ab/a= )"
  print "		2: variable multiplication (ab/x=a)"
  print "		3: variable division (ax=ab)"
  print "		4: mixed drills"
  print "-q \"<quot>\", --quote \"<quote>\":		Quote to use in games that use quotes."
  print "-g <id>, --game <id>:		Generate a game:"
  print "		0: No game (default)"
  print "		1: 'crostic' type puzzle"
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
  print "		a: nnn*nn or x/nn=nnn"
  print "		b: Unit rate exercises"
  print "		c: Perfect squares"
  print "		d: x^2+a=b"
  print "	Examples: \"-t 138af\" \"-t 2\""

if __name__ == "__main__":
  print "\nLoading Algebra Exercise Generator v%s..." % (ver)
  main(sys.argv[1:])