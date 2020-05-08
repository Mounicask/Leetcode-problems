# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         

def level(root,val,lev):
    if root is None : 
        return 0 
    if root.val == val:
        return lev
    
    l = level(root.left, val, lev+1) 
    if l != 0: 
        return l 
    return level(root.right,val,lev + 1)
    
def sibling(root,x,y):
    if root is None:
        return 0
    
    return ((root.left.val == x and root.right.val == y) or (root.left.val == x and root.right.val == y) or sibling(root.left,x,y) or sibling(root.right,x,y) )
    
    
def isCousins(root, x, y) :
    if level(root,x,1) == level(root, y, 1) and  sibling(root,x,y) == True :
            print("Yes")
    else:
        print("No")


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
val = isCousins(root,3,4)

print("Val is ",val)

def isSibling(root, a , b): 
  
    # Base Case 
    if root is None: 
        return 0
  
    return ((root.left == a and root.right ==b) or 
            (root.left == b and root.right == a)or
            isSibling(root.left, a, b) or
            isSibling(root.right, a, b)) 
    
    
 def isSibling(root,x,y):
        if root is None:
            return 0

        return ((root.left.val == x and root.right.val == y) or 
                (root.left.val == x and root.right.val == y) or  
                isSibling(root.left,x,y) or
                isSibling(root.right,x,y) )
       
    
    
    
    