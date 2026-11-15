# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return root
        # case 1: no child node
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            #case 2: 1 child node
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            #case 3: 2 child nodes 
            #going to the right side
            cur = root.right
            #iterate to the minimum number in the right side
            while cur.left:
                cur = cur.left
            # assign the current val (leaf node) in the current root
            root.val = cur.val
            #delete the value 
            root.right = self.deleteNode(root.right, root.val)
        
        return root

        