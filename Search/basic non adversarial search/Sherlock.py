# I decided to use GBFS using Manhattan distance as a heuristic because he wants to get there ASAP and the 
# cost probably does not really matter to him. 

city_map = {
    'S': ['A', 'B'],
    'A': ['S', 'C'],
    'B': ['S', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['B', 'C']
}

initial_state = 'S'
goal_state = 'C' 

def manhattan_distance_to_C(state):
    if state in ['S','B','D']:
        return 2
    elif state in ['A','E']:
        return 1
    else: 
        return 0

def find_index(list_of_lists, h):
    l = len(list_of_lists)
    if l == 0:
        return 0
    for i in range(l):
        if h <= list_of_lists[i][1]:
            return i
    return l
    
def GBFS(start, goal):
    current = start
    frontier = []
    explored = [] 
    while True:
        if current == goal: 
            # do I print the optimal solution? call a function for that?
            explored.append(current)
            break
        explored.append(current)
        for node in city_map[current]:
            if(node in explored):
                continue
            h = manhattan_distance_to_C(node)
            index = find_index(frontier,h)
            frontier.insert(index,[node,h])
        if len(frontier) == 0:
            return '\0'
        current = frontier.pop(0)[0]
    return explored

def main():
    explored = GBFS(initial_state,goal_state)
    if explored != '\0':
        for node in explored:
            print(node)
    else:
        raise Exception("Goal state not found")
    
    
if __name__ == "__main__":
    main()