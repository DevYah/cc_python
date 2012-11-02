def dis(ar):
  for a in ar: 
    print a

img = [[1,2,3], [6,7,8], [9,10,11]]
#img = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
n = len(img)

# not in place
def rotate_90(img):
  i, j = 0, 0
  n_img = [[0 for x in xrange(0,n)] for y in xrange(0,n)]

  while i < n: 
    j = 0
    while j < n: 
      n_img[j][n-i-1] = img[i][j]
      j+=1
    i+=1
  return n_img

# in place
def rotate_90_2(img):
  l = 0 # level
  while l < 2:
    i = l
    while i < n-l-1:
      temp = img[l][i]
      img[l][i] = img[n-i-1][l]
      img[n-i-1][l] = img[n-l-1][n-i-1] 
      img[n-l-1][n-i-1] = img[i][n-l-1]
      img[i][n-l-1] = temp

      print "temp is %d" % temp
      i +=1
    l+=1
  return img

dis(img)
n_img = rotate_90_2(img)
print '-------------'
dis(n_img)

