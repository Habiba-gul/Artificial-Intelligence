import math

class CityNode:
    def __init__(self, city, parentNode, neighbours, pathCost):
        self.city = city
        self.parentNode = parentNode
        self.neighbours = neighbours
        self.pathCost = pathCost


def getLowestCost(frontier):
    minimum = math.inf
    selected = ""

    for node in frontier:
        if frontier[node][1] < minimum:
            minimum = frontier[node][1]
            selected = node

    return selected


def tracePath(graphData, start, destination):
    route = [destination]
    parentCity = graphData[destination].parentNode

    while parentCity is not None:
        route.append(parentCity)
        parentCity = graphData[parentCity].parentNode

    route.reverse()
    return route


def uniformCostSearch():
    start = "Arad"
    destination = "Bucharest"

    graphData = {
        'Oradea': CityNode('Oradea', None, [('Zerind', 71), ('Sibiu', 151)], 0),
        'Zerind': CityNode('Zerind', None, [('Oradea', 71), ('Arad', 75)], 0),
        'Arad': CityNode('Arad', None, [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)], 0),
        'Sibiu': CityNode('Sibiu', None, [('Oradea', 151), ('Arad', 140), ('Fagaras', 99), ('Rimnicu Vilcea', 80)], 0),
        'Timisoara': CityNode('Timisoara', None, [('Arad', 118), ('Lugoj', 111)], 0),
        'Fagaras': CityNode('Fagaras', None, [('Sibiu', 99), ('Bucharest', 211)], 0),
        'Lugoj': CityNode('Lugoj', None, [('Timisoara', 111), ('Mehadia', 70)], 0),
        'Mehadia': CityNode('Mehadia', None, [('Lugoj', 70), ('Drobeta', 75)], 0),
        'Drobeta': CityNode('Drobeta', None, [('Mehadia', 75), ('Craiova', 140)], 0),
        'Rimnicu Vilcea': CityNode('Rimnicu Vilcea', None, [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)], 0),
        'Craiova': CityNode('Craiova', None, [('Rimnicu Vilcea', 146), ('Drobeta', 120), ('Pitesti', 138)], 0),
        'Pitesti': CityNode('Pitesti', None, [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)], 0),
        'Bucharest': CityNode('Bucharest', None, [('Pitesti', 101), ('Fagaras', 211), ('Giurgiu', 90), ('Urziceni', 85)], 0),
        'Giurgiu': CityNode('Giurgiu', None, [('Bucharest', 90)], 0),
        'Urziceni': CityNode('Urziceni', None, [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)], 0),
        'Hirsova': CityNode('Hirsova', None, [('Urziceni', 98), ('Eforie', 86)], 0),
        'Eforie': CityNode('Eforie', None, [('Hirsova', 86)], 0),
        'Vaslui': CityNode('Vaslui', None, [('Urziceni', 142), ('Iasi', 92)], 0),
        'Iasi': CityNode('Iasi', None, [('Vaslui', 92), ('Neamt', 87)], 0),
        'Neamt': CityNode('Neamt', None, [('Iasi', 87), ('Fagaras', 211)], 0)
    }

    frontier = {}
    frontier[start] = (None, 0)

    visited = []

    while len(frontier) != 0:

        currentNode = getLowestCost(frontier)
        del frontier[currentNode]

        if graphData[currentNode].city == destination:
            return tracePath(graphData, start, destination)

        visited.append(currentNode)

        for neighbour in graphData[currentNode].neighbours:

            newCost = neighbour[1] + graphData[currentNode].pathCost

            if neighbour[0] not in frontier and neighbour[0] not in visited:

                graphData[neighbour[0]].parentNode = currentNode
                graphData[neighbour[0]].pathCost = newCost

                frontier[neighbour[0]] = (
                    graphData[neighbour[0]].parentNode,
                    graphData[neighbour[0]].pathCost
                )

            elif neighbour[0] in frontier:

                if frontier[neighbour[0]][1] > newCost:

                    frontier[neighbour[0]] = (currentNode, newCost)

                    graphData[neighbour[0]].parentNode = currentNode
                    graphData[neighbour[0]].pathCost = newCost


if __name__ == "__main__":
    answer = uniformCostSearch()
    print(answer)