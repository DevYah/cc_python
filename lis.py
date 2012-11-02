from bisect import bisect_left

s1 = '12345222'

def all_subs(org, s, i, sset):
  if ''.join(sorted(s)) == s:
    sset.add(s)
  if i == len(s1):
    return 0

  all_subs(org, s+org[i], i+1, sset)
  all_subs(org, s, i+1, sset)

sset = set() 
all_subs(s1, '', 0, sset)
print sorted(sset, key= lambda x: (len(x), x))




s1 = '12345222'
dp= [1 for y in xrange(0,len(s1))]

def dp_lis(s1):
  global dp
  for i in xrange(0, len(s1)):
    for j in xrange(0,i):
      if dp[i] <= dp[j] and  s1[i] >= s1[j]:
        dp[i] = dp[j] + 1
 
  maxi = 0
  for i in xrange(0,len(dp)):
    if dp[i] > dp[maxi]: 
      maxi = i
  
  res = s1[maxi]
  for i in xrange(maxi-1,-1,-1):
    if s1[i] < res[0]:
      res = s1[i] + res
  return res



print dp_lis(s1)
