# Problem: Serialize and Deserialize Binary Tree
# Source: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Topic: Tree, BFS, String
# Status: ✅ Done

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        # BFS level-order serialization
        if not root:
            return "null"
        result = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("null")
        return ",".join(result)

    def deserialize(self, data):
        # BFS level-order deserialization, the inverse of serialize
        vals = data.split(",")
        if vals[0] == "null":
            return None
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q and i < len(vals):
            node = q.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if i < len(vals) and vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root
