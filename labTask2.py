import math

class Node:
    def __init__(self, state, parent, actions, totalCost, heuristic):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
        self.heuristic = heuristic

def findMin(frontier):
    minV = math.inf
    node = ''
    for i in frontier:
        if minV > frontier[i][1]:
            minV = frontier[i][1]
            node = i
    return node

def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent is not None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

def euclidean_heuristic(current, goal):
    return math.sqrt((current[0] - goal[0])**2 + (current[1] - goal[1])**2)

def Astar_maze():
    start = (0, 0)
    goal = (9, 9)   
    
    
    maze = [
      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
      [0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
      [0, 1, 0, 0, 1, 0, 0, 0, 1, 1],
      [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 1, 1, 1, 0, 1, 1],
      [1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
      [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
      [1, 0, 1, 1, 1, 0, 0, 0, 1, 0],
    ]  
    valid_positions = [(i,j) for i in range(10) for j in range(10) if maze[i][j] == 0]
    
    
    graph = {}
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    
    for pos in valid_positions:
        actions = []
        for dx, dy in directions:
            ni, nj = pos[0]+dx, pos[1]+dy
            if (ni, nj) in valid_positions:   
                actions.append(((ni,nj), 1))
        graph[pos] = Node(pos, None, actions, 0, pos)
    
    
    frontier = {}
    heuristicCost = euclidean_heuristic(start, goal)
    frontier[start] = (None, heuristicCost)
    
    explored = {}
    
    while frontier:
        currentNode = findMin(frontier)
        del frontier[currentNode]
        
        if currentNode == goal:
            path = actionSequence(graph, start, goal)
            total_cost = graph[goal].totalCost
            print("Path found:", path)
            print("Total cost:", total_cost)
            return path, total_cost
        
        currentCost = graph[currentNode].totalCost
        h = euclidean_heuristic(currentNode, goal)
        explored[currentNode] = (graph[currentNode].parent, currentCost + h)
        
        for child, move_cost in graph[currentNode].actions:
            newCost = currentCost + move_cost
            child_h = euclidean_heuristic(child, goal)
            f = newCost + child_h
            
            if child in explored and explored[child][1] <= f:
                continue
            if child not in frontier or frontier[child][1] > f:
                graph[child].parent = currentNode
                graph[child].totalCost = newCost
                frontier[child] = (currentNode, f)
    
    print("No path found!")
    return None, None


solution_path, path_cost = Astar_maze()