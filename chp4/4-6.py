def low_anc(head, node1, node2):
  left, right = head.left, head.right
  
  if is_reachable(left, node1) and is_reachable(left, node2): 
    return low_anc(left, node1, node2)
  
  if is_reachable(right, node1) and is_reachable(right, node2): 
    return low_anc(right)
    
  return head
  

def is_reachable(start, end):
  if start is None: 
    return False
    
  if start is end: 
    return True
        
  return is_reachable(start.left, end) or is_reachable(start.right, end)
  
  
