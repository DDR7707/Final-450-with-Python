class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def bfs(image , m , n , i , j , p , f):
            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] == f or image[i][j] != p:
                return
            image[i][j] = f
            bfs(image , m , n , i-1 , j , p , f)
            bfs(image , m , n , i+1 , j , p , f)
            bfs(image , m , n , i , j-1 , p , f)
            bfs(image , m , n , i , j+1 , p , f)
        
        m = len(image)
        n = len(image[0])
        bfs(image , m , n , sr , sc , image[sr][sc] , newColor)
        return image
