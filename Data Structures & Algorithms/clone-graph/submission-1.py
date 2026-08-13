"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mem = {}
        def clone(graph):
            if graph in mem:
                return mem[graph]
            root = Node(graph.val)
            mem[graph] = root

            for neighbor in graph.neighbors:
                root.neighbors.append(clone(neighbor))
            return root
        return clone(node) if node else None
        