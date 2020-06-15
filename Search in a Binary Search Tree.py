Search in a Binary Search Tree

Solution
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. 

If such node doesn't exist, you should return NULL.


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.val == val:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)