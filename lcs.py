a = 'abdcedes'
b = 'asdbse'


def bad_lcs(s1,s2, i1, i2, r, seq):
  if i1 == len(s1) or i2 == len(s2):
    return (seq, r)
  
  if (s1[i1] == s2[i2]):
    return bad_lcs(s1, s2, i1+1, i2+1, r+1, seq+s1[i1])
  else:
    if i2+1 < len(s2) and i1+1 < len(s1):
      return max(bad_lcs(s1, s2, i1, i2+1, r, seq),
          bad_lcs(s1, s2, i1+1, i2, r, seq), key=lambda x: x[1])

    elif i2+1 < len(s2):
      return bad_lcs(s1, s2, i1, i2+1, r, seq)
    else:
      return bad_lcs(s1, s2, i1+1, i2, r, seq)



dp= [[0 for x in xrange(0,len(a)+1)] for y in xrange(0,len(b)+1)]
def dp_lcs(s1,s2):
  global dp
  i,j=1,1
  while i <= len(b):
    j=1
    while j <= len(a):
      if b[i-1] == a[j-1]:
        dp[i][j] = dp[i-1][j-1]+1
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
      j+=1
    i+=1

  print "      %s" % (', '.join(a))
  i = 0  
  for x in dp:
    if i == 0:
      print "  %s" % (x)
    else:
      print "%s %s" % (b[i-1], x)
    i +=1

  result = ''
  i,j = len(b), len(a)
  while i >= 0 and j >= 0:
    print i,j
    if dp[i][j] == dp[i-1][j]:
      i = i-1
    elif dp[i][j] == dp[i][j-1]:
      j = j -1
    else:
      print '(%d, %d) %s' %  (i, j,b[i-1])
      result = b[i-1] + result
      i = i-1
      j = j-1
  return result


print dp_lcs(a,b)
      
#print "   %s" % (', '.join(a))
#i = 0  
#for x in dp:
#  print "%s %s" % (b[i], x)
#  i += 1  


print bad_lcs(a,b,0,0,0,'')
