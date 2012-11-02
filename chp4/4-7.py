def is_subtree(t1, t2):
  if t2 is None: 
    return True
  
  if t1 is None:
    return False
    
  if is_match(t1, t2):
    return True
  else: 
    return is_subtree(t1.left, t2) or is_subtree(t1.right, t2)
    

  
def is_match(r1, r2): 
  if r1 is None and r2 is None: 
    return True
  if r1 is None or r2 is None: 
    return False
    
    
  if r1.data == r2.data: 
    return is_match(r1.left, r2.left) and is_match(r1.right, r2.right)
    

