class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_h = self.get_height(root.left)
        right_h = self.get_height(root.right)
        
        if left_h == right_h:
            return (1 << left_h) + self.countNodes(root.right)
        else:
            return (1 << right_h) + self.countNodes(root.left)

    def get_height(self, node: Optional[TreeNode]) -> int:
        height = 0
        while node:
            height += 1
            node = node.left
        return height