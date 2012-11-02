

def permute(ss, es, lis):
  if len(es) == 1:
    lis.append(ss+es)

  for i in xrange(0,len(es)):
    temp = ''.join([es[0:i],es[i+1:]])
    permute(''.join([ss,es[i]]), temp, lis) 



l = []
word = 'abcd'
permute('', word, l)
for x in l: print x


