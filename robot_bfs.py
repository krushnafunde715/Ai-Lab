#robot path planning using bfs

# 0 = free path  1 = obstacle

grid = [
    [ 0 , 0 , 1 , 0 ],
    [ 1 , 0 , 1 , 0 ],
    [ 1 , 0 , 0 , 1 ],
    [ 1 , 1 , 0 , 0 ],
]

start = (0,0)
goal = (3,3)

position = start

queue = [start]
visited = [start]

moves = [ (0,1), (1,0), (0,-1), (-1,0) ]

print("\n=====Robot path planning using BFS=====\n")

while queue:

    position = queue.pop(0)
    print("Robot is at", position)

    if position == goal :
        print("Path find and goal reached!!")
        break

    for move in moves:
        row = position[0] + move[0]
        col = position[1] + move[1]

        if( 0 <= row < 4 and 0 <= col < 4 and grid[row][col] == 0 ):
            new_position = (row,col)

            if new_position not in visited:
                queue.append(new_position)
                visited.append(new_position)

else:
    print("Path not found")


print("\nVisited positions:")
print(visited)