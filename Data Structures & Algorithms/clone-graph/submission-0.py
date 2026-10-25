"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #going through each neighbors
        #how can we prevent looping??
        #have a set val??
        if not node:
            return None
        visited = {}
        
        def dfs(curr):
            # Step 1: If curr was already cloned,
            if curr in visited:
                return visited[curr]
            # return its existing clone.

            # Step 2: Create a clone of curr.
            clone = Node(curr.val)
            # Step 3: Store original -> clone
            # in visited BEFORE recursing.
            visited[curr] = clone
            # Step 4: Go through curr.neighbors.
            for n in curr.neighbors:
            # For each neighbor, obtain its clone
                clone2 = dfs(n)
            # using dfs and connect it to this clone.
                clone.neighbors.append(clone2)
            # Step 5: Return this clone.
            return clone

        return dfs(node) 

