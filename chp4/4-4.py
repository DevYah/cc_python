from collections import deque
class Node(object):
  def __init__(self, value, left=None, right=None): 
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    return "[Node (%s)]" % str(self.value)

# 4-4
lls = []
def make_ll(node, steps):
  q = deque()
  level = 0
  q.append((node,level))
  while q:
    tmp = q.pop()
    if tmp[0] is None: 
      continue
    print "temp is %s, %s" % (tmp[0], tmp[1])
    level = tmp[1]
    
    if len(lls) <= level:
      lls.append([tmp[0].value])
    else:
      lls[level].append(tmp[0].value)
      
    q.appendleft((tmp[0].left, level+1))
      
    q.appendleft((tmp[0].right, level+1))

a = Node(4)
b = Node(2)
c = Node(1)
d = Node(3)
e = Node(6)
f = Node(5)
g = Node(7)

a.left = b 
a.right = e

b.left = c
b.right = d

e.left = f
e.right = g

print lls
make_ll(a, 0)

for x in lls:
  print x 
