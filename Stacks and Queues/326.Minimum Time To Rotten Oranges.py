class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rotten = set()
        count = 0
        
        for r,row in enumerate(grid):
            for c,v in enumerate(row):
                if v == 1:
                    fresh.add((r,c))
                if v == 2:
                    rotten.add((r,c))
                    
        while rotten and fresh:
            new_rot = set()
            for r,c in rotten:
                for i,j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new = (r+i , c+j)
                    
                    if new in fresh:
                        fresh.remove(new)
                        new_rot.add(new)
                        
            rotten = new_rot
            count += 1
            
        return count if not fresh else -1 
