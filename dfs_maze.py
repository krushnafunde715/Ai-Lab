# dfs- maze problem 

maze = [
    [ 0 , 0 , 1 , 0],
    [ 1 , 0 , 1 , 0],
    [ 1 , 0 , 1 , 0],
    [ 1 , 0 , 0 , 0]
]

start = (0,0)
goal = (3,3)

position = start

stack = [start]
visited = [start]

moves = [ (0,1), (1,0), (0,-1), (-1,0) ]

print("======Maze solution using DFS======")

while stack:

    position = stack.pop()
    print("Agent is at", position)

    if (position == goal):
        print("Goal Achieved !!!")
        break

    for move in moves:
        row = position[0] + move[0]
        col = position[1] + move[1]

        if( 0 <= row < 4 and 0 <= col < 4 and maze[row][col] == 0 ):
            new_position = (row,col)

            if new_position not in visited:
                stack.append(new_position)
                visited.append(new_position)

else:
    print("Goal cannot be reached !!")


#final path

print("\nVisited positions:")
print(visited)
