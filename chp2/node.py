class Node:
  def __init__(self, data, next=None):
    self.next = next
    self.data = data
  def __str__(self):
    if self.next == None:
      return "%d" % self.data
    else:
      return "%d => %s" % (self.data, self.next.__str__())

a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(2)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

b1 = Node(5)
b2 = Node(9)
b3 = Node(5)

b1.next = b2
b2.next = b3
 

#2-1
def rm_dups(node):
  hash = {}
  hash[node.data] = 1

  while node.next != None:
    if hash.has_key(node.next.data):
      node.next = node.next.next
    else:
      hash[node.next.data] = True
      node = node.next

#2-1'
def rm_dups2(node):
  current = node
  while current is not None: 
    loop_node = current
    while loop_node.next is not None: # or loop_node.next 
      if loop_node.next.data == current.data:
        loop_node.next = loop_node.next.next      
       
      if loop_node.next == None:
        break
      loop_node = loop_node.next


    current = current.next

        
        
#2-2
def get_nth(n, head):
  size = 0
  current = head
  while current != None:
    size +=1
    current = current.next
  current, i = head, 0
  
  while i != size -1 - n:
    i +=1
    current = current.next

  return current

#2-3
def del_node(node):
  if node == None or node.next == None:
    return False

  node.data = node.next.data
  node.next = node.next.next
  return True

#2-4
def add_nums(y,z, carry):
  if y is None and z is None:
    if carry == 1:
      return Node(1)
    else:
      return None

  res = Node(carry)
  value = carry
  if y is not None:
    value += y.data
  if z is not None:
    value +=  z.data

  res.data = value % 10
  carry = value / 10
  rest = add_nums(y.next, z.next, carry)
  res.next = rest
  return res
    
#2-4'
def add_nums2(y,z):
  head = Node(0)
  res = head
  yc = y
  zc = z
  carry = 0
  while True:
    value = carry
    if yc is not None:
      value += yc.data
      yc = yc.next
    if zc is not None: 
      value += zc.data
      zc = zc.next

    res.data = value % 10
    carry = value / 10
    if zc is None and yc is None:
      if carry == 0:
        res.next = None
      else:
        res.next = Node(carry) 
      break
    else:
      res.next = Node(carry) 

    res = res.next

  return head


#2-5
def get_start(circle):
  hash = {}
  current = circle
  while current not in hash:
    hash[current] = True
    current = current.next

  return current

