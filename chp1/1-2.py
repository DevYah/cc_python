def rev(wrd):
  for i in xrange(0, len(wrd)/2):
    temp = wrd[i]
    wrd[i] = wrd[len(wrd)-i-2]
    wrd[len(wrd)-i-2] = temp

word = list('abcd*')
print "".join(word)
rev(word)
print "".join(word)
