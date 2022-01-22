class ratInMaze:
    def isSafe(self,visited,i,j,n):
        if i>=0 and j>=0 and i<n and j<n and visited[i][j] == 0:
            return True
        return False
    def helper(self,Maze,i,j,n,visited,answers,ans):
        if i == n-1 and j == n-1:
            answers.append(ans)
            return answers

        if not self.isSafe(visited,i,j,n):
            return answers

        visited[i][j] = 1
        #Move Up
        if i>=1 and Maze[i-1][j] == 1:
            self.helper(Maze,i-1,j,n,visited,answers,ans+"U")

        #Move Down
        if i < n-1 and Maze[i+1][j] == 1:
            self.helper(Maze,i+1,j,n,visited,answers,ans+"D")
        #Move Left
        if j>=1 and Maze[i][j-1] == 1:
            self.helper(Maze,i,j-1,n,visited,answers,ans+"L")
        #Move Right
        if j<n-1 and Maze[i][j+1] == 1:
            self.helper(Maze,i,j+1,n,visited,answers,ans+"R")

        visited[i][j] = 0
        return answers




    def move(self,Maze):
        n = len(Maze)
        print(n)
        # Creating Visited Array
        visited = []
        for i in range(n):
            visited.append([])
            for j in range(n):
                visited[i].append(0)
        return self.helper(Maze,0,0,n,visited,[],"")
        

        

if __name__ == "__main__":
    A = ratInMaze()
    a = [[1,1,1,1],[1,1,1,0],[1,0,1,0],[1,0,1,1]]
    print(A.move(a))

    

    