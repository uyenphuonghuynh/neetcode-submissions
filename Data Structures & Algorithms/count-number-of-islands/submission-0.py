class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        r, c = len(grid), len(grid[0])
        #how do i know which island i already count
        #adding it's neighbor to a set?
        count = set() #taking O(n)

        def neighbour(nr, nc):
            #checking requirement:
            if nr >= r or nc >= c or nr < 0 or nc < 0:
                return
            #checking water or land
            if grid[nr][nc] == '0':
                return
            if (nr,nc) in count:
                return
            count.add((nr, nc))
            neighbour(nr+1, nc)
            neighbour(nr-1, nc)
            neighbour(nr, nc+1)
            neighbour(nr, nc-1)
        
        for nr in range(r):
            for nc in range(c):
                #checking requirement:
                if nr > r or nc > c or nr < 0 or nc < 0:
                    continue
                #checking water or land
                if grid[nr][nc] == '0':
                    continue
                if (nr,nc) in count:
                    continue
                #adding the neighbour 1s to the set
                neighbour(nr, nc)
                #increase island 
                island += 1
        return island

        
            










