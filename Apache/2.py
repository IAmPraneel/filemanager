def astar(grid, start, goal):

    open_set = []
    came_from = {}
    g_score = {}
    g_score[start]=0
    open_set.append(start)

    while len(open_set)>0:
        curr = open_set[0]

        # Selecting the best next node f(x)=g(x)+h(x)
        for node in open_set:
            f_curr = g_score[curr]+abs(curr[0]-goal[0]) + abs(curr[1]-goal[1])
            f_node = g_score[node]+abs(node[0]-goal[0]) + abs(node[1]-goal[1])
            if f_node<f_curr:
                curr = node
        open_set.remove(curr)
        # if curr == goal build path
        if curr == goal:
            path = []
            while curr in came_from:
                path.append(came_from[curr])
                curr = came_from[curr]
            path.append(start)
            path.reverse()
            return path
        # explore next step
        x = curr[0]
        y = curr[1]
        for step in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx = x + step[0]
            ny = y + step[1]
            if nx>=0 and ny>=0 and nx<n and ny<n and grid[nx][ny]==0:
                temp_g = g_score[curr]+1
                if (nx,ny) not in g_score or temp_g<g_score[(nx,ny)]:
                    g_score[(nx,ny)]=temp_g
                    came_from[(nx,ny)]=curr
                    if (nx,ny) not in open_set:
                        open_set.append((nx,ny))
    return None

n = int(input("Enter number of rows and columns: "))
grid = []
for i in range(n):
    row = []
    row_ = input("Enter row as 0/1: ").split()
    for j in range(n):
        row.append(int(row_[j]))
    grid.append(row)

start_ = input("Enter start node as x y: ").split()
start = (int(start_[0]),int(start_[1]))

goal_ = input("Enter goal node as x y: ").split()
goal = (int(goal_[0]),int(goal_[1]))

path = astar(grid,start,goal)

for i in path:
    grid[i[0]][i[1]]='x'

for i in grid:
    print(i)
