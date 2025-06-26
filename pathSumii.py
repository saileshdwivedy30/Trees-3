# Time Complexity : O(n), where n is the number of nodes in the tree
# Space Complexity : O(h), where h is the height of the tree (for recursion stack)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, path, current_sum):
            if not node:
                return
            path.append(node.val)
            current_sum += node.val

            # Check if it's a leaf and the path sums to targetSum
            if not node.left and not node.right and current_sum == targetSum:
                result.append(path[:])  # Make a copy of the path
            else:
                dfs(node.left, path, current_sum)
                dfs(node.right, path, current_sum)

            # Backtrack
            path.pop()

        dfs(root, [], 0)
        return result
