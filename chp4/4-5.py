def get_successor(node):
  if node.right is not None: 
    return left_most(node.right)
  
  if node.parent.left is node: 
    return node.parent
  
  if node.parent.right is node:
    return get_successor(parent)
    
  return None
  
def left_most(node):
  if node is None: 
    return None
    
  if node.left is None: 
    return node
    
  return left_most(node.left)

