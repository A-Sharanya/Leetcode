class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        if not root:
            return []
            
        paths = []
        
        def dfs(node, current_path):
            if not node.left and not node.right:
                paths.append(current_path + str(node.val))
                return
                
            next_path = current_path + str(node.val) + "->"
            
            if node.left:
                dfs(node.left, next_path)
            if node.right:
                dfs(node.right, next_path)
                
        dfs(root, "")
        return paths