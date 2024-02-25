from demo import maze, COLOR, agent
from collections import deque
from queue import PriorityQueue
                                ######################################################

# UCS Function
def UCS(Maze, *Age, start = None):
    if start is None:
        start = (Maze.rows, Maze.cols);
    hurd = [(i.position, i.cost) for i in Age];

    uncheck = {nod:float('inf') for nod in Maze.grid};
    uncheck[(Maze.rows, Maze.cols)] = 0;
    check = {};
    rev = {};

    while uncheck:
        currnod = min(uncheck, key = uncheck.get);
        check[currnod] = uncheck[currnod];
        if currnod == Maze._goal:
            break;
        for dir in 'NEWS':
            if Maze.maze_map[currnod][dir] == True:
                if dir == 'E':
                    newnod = (currnod[0], currnod[1] + 1);
                elif dir == 'W':
                    newnod = (currnod[0], currnod[1] - 1);
                if dir == 'S':
                    newnod = (currnod[0] + 1, currnod[1]);
                elif dir == 'N':
                    newnod = (currnod[0] - 1, currnod[1]);
                if newnod in check:
                    continue;
                dist = uncheck[currnod] + 1;
                for hurdle in hurd:
                    if hurdle[0] == currnod:
                        dist = dist + hurdle[1];
                if dist < uncheck[newnod]:
                    uncheck[newnod] = dist;
        uncheck.pop(currnod);

    fwd = {};
    cell = Maze._goal;
    while cell != start:
        fwd[rev[cell]] = cell;
        cell = rev[cell];
    return fwd, check[(1, 1)];
                                ######################################################

# DFS Function
def DFS(m):
    start = (m.rows, m.cols);
    explored = [start];
    front = [start];
    dfs ={};
    while len(front) > 0:
        currnod = front.pop();
        if currnod == (1, 1):
            break;
        for dir in 'NEWS':
            if m.maze_map[currnod][dir] == True:
                if dir == 'E':
                    newnod = (currnod[0], currnod[1] + 1);
                elif dir == 'W':
                    newnod = (currnod[0], currnod[1] - 1);
                if dir == 'S':
                    newnod = (currnod[0] + 1, currnod[1]);
                elif dir == 'N':
                    newnod = (currnod[0] - 1, currnod[1]);
                if newnod in explored:
                    continue;
                explored.append(newnod);
                front.append(newnod);
                dfs[newnod] = currnod
        
    fwd = {};
    cell = (1, 1);
    while cell != start:
         fwd[dfs[cell]] = cell;
         cell = dfs[cell];
    return fwd;
                                ######################################################

# BFS Function
def BFS(m, start = None):
    start = (m.rows, m.cols)
    front = [start]
    bfs = {}
    explored = [start]

    while len(front) > 0:
        currnod=front.pop(0)
        if currnod == (1, 1):
            break
        for d in 'ESNW':
            if m.maze_map[currnod][d] == True:
                if d == 'E':
                    newnod = (currnod[0], currnod[1] + 1)
                elif d == 'W':
                    newnod = (currnod[0], currnod[1] - 1)
                elif d == 'S':
                    newnod = (currnod[0] + 1, currnod[1])
                elif d == 'N':
                    newnod = (currnod[0] - 1, currnod[1])
                if newnod in explored:
                    continue;
                front.append(newnod)
                explored.append(newnod)
                bfs[newnod] = currnod
    fwd = {}
    cell = (1, 1)
    while cell != (m.rows , m.cols):
        fwd[bfs[cell]] = cell
        cell = bfs[cell]
    return fwd

                                ######################################################

# Heuristic Function
def h(nod1, nod2):
    x1, y1 = nod1;
    x2, y2 = nod2;
    return abs((x2 - x1) + (y2 - y1));  # returns the abs of manhattan distance


# Greedy
# We only consider the heuristic cost of each node and then we continue accordingly
def Greedy(m):
    start = (m.rows, m.cols);       # initialized to last row and last col value
    #g_score = {cell :float('inf') for cell in m.grid};
    #g_score[start] = 0;
    f_score = {cell:float('inf') for cell in m.grid};
    f_score[start] = h(start, (1, 1));
    apth = {};
    open = PriorityQueue();
    open.put((h(start, (1, 1)), h(start, (1, 1)), start));
    while not open.empty():
                 currnod = open.get()[2];
                 if currnod == (1, 1):
                     break;
                 for dir in 'NEWS':
                     if m.maze_map[currnod][dir] == True:
                         if dir == 'E':
                             newnod = (currnod[0], currnod[1] + 1);
                         if dir == 'W':
                             newnod = (currnod[0], currnod[1] - 1);

                         if dir == 'S':
                             newnod = (currnod[0] + 1, currnod[1]);

                         if dir == 'N':
                             newnod = (currnod[0] - 1, currnod[1]);
                         #temp_g_score = g_score[currnod] + 1;
                         temp_f_score = h(newnod, (1, 1));
                         if temp_f_score < f_score[newnod]:
                             #g_score[newnod] = temp_g_score;
                             f_score[newnod] = temp_f_score;
                             open.put((temp_f_score, h(newnod, (1, 1)), newnod));
                             apth[newnod] = currnod;
    fwd = {};
    cell = (1, 1);
    while cell != start:
        fwd[apth[cell]] = cell;
        cell = apth[cell];
    return fwd;


                                ######################################################
# Main Programme
if __name__== '__main__':
    #m1 = maze(10, 10)
    #m1.CreateMaze(loopPercent = 100);
    #A1 = agent(m1, 10, 10, color = 'blue');
    #A2 = agent(m1, 10, 9, color = 'red');

    # UCS Function kee functionality
    #A1 = 200;
    #path, var = UCS(m1, A1, A2);
    #a = agent(m1, color = COLOR.yellow, filled = True, footprints = True);

    # BFS Function kee functionality
    
    m2 = maze(10,10)
    m2.CreateMaze(loopPercent = 10,theme='light')
    path = BFS(m2)
    a = agent(m2, footprints = True, color = COLOR.green, shape = 'square', filled = True)
    m2.tracePath({a:path})
    m2.run()

    # DFS Function kee functionality
    m3 = maze(10,10)
    m3.CreateMaze(loopPercent = 10,theme='light')
    path1 = DFS(m3)
    a1 = agent(m3, footprints = True, color = COLOR.yellow, shape = 'square', filled = True)
    m3.tracePath({a1:path1})
    m3.run()

    # Greedy
    m4 = maze(10, 10);
    m4.CreateMaze();
    path2 = Greedy(m4);

    a2 = agent(m4, footprints = True);
    m4.tracePath({a2:path2});
    m4.run();
