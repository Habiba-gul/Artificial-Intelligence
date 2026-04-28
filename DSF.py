class Node:
    def __init__(self,state,parent,actions,totalCost):
        self.state = state
        self.parent=parent
        self.actions=actions
        self.totalCost=totalCost

def actionSeq(graph,initial,goal):
    sol=[goal]
    currentP=graph[goal].parent
    while currentP!=None:
        sol.append(currentP)
        currentP=graph[currentP].parent
    sol.reverse()
    return sol        
def DFS():
    initial='D'
    goal='G'
    graph = { 'A': Node('A',None,['B','E','C']),
              'B': Node('B',None,['A','D','E']),
              'C': Node('C',None,['F','G','A']),
              'D': Node('D',None,['B','E']),
              'E': Node('E',None,['A','B','D']),
              'F': Node('F',None,['C']),
              'G': Node('G',None,['C'])
    }
    frontier=[initial]
    explored=[]
    while len(frontier)!=0:
        current = frontier.pop(len(frontier)-1)
        print(current)
        explored.append(current)
        currentChildern=0
        actions = graph[current].actions
        for child in actions:
            if child not in frontier and child not in explored:
                graph[child].parent=current
                if graph[child].state==goal:
                    return actionSeq(graph,initial,current)
                currentChildern=currentChildern+1
                frontier.append(child)
        if currentChildern==0:
            del(explored[len(explored)-1])

if __name__ == "__main__":
    result = DFS()
    result.append('F')
    print(result)