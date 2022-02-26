def solution(Board):
    res = float('-inf')
    for i in range(len(Board)):
        for j in range(len(Board[0])):
            seen = [[False]* len(Board[0]) for _ in range(len(Board))]
            res = max(res, greatest(Board, i, j, seen, ''))
    return res

def greatest(Board, r, c, seen, cur):
    if r < 0 or c < 0 or r >= len(Board) or c >= len(Board[0]) or seen[r][c]:
        return 0
    cur += str(Board[r][c])
    if len(cur) == 4:
        return int(cur)
    
    stack = []
    neighbors = ((1, 0), (0, 1), (-1, 0), (0, -1))
    seen[r][c] = True
    for dr, dc in neighbors:
        stack.append(greatest(Board, dr+r, dc+c, seen, cur))
    
    return max(stack)

'''Board = [[9,1,1,0,7],
         [1,0,2,1,0],
         [1,9,1,1,0]]
print(solution(Board))'''

Board = [[0,1,5,0,0]]
print(solution(Board))