class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        output = []
        
        def dfs(node):
            if not node: return
            output.append(node.val)
                
            for c in node.children:
                dfs(c)
        dfs(root)
        
        return output
        
