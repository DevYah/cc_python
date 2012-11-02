def dis(array):
  for x in array:
    print x
  print "-------------"

a = [[1,0,3,4],[5,2,4,5],[1,2,3,2]]
dis(a)


i,j = 0,0
cols = []
rows = []

for i in xrange(0, len(a)):
  for j in xrange(0, len(a[i])):
    if a[i][j] == 0:
      rows.append(i)
      cols.append(j)

for r in rows: 
  a[r] = [0]*len(a[r])

for c in cols:
  for i in xrange(0,len(a)):
      a[i][c] = 0

dis(a)
