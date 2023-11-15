# I decided to use BFS because she wants to explore. From the prompt, I understand she does not know any heuristic. 

tree = {
    'A':['B','C'],
    'B':['D'],
    'C':['E','F'],
    'D':['H','G'],
    'E':[],
    'F':['T'],
    'G':[],
    'H':[],
    'T':[]
}

initial_state = 'A'
goal_state = 'T' 

def BFS(start, goal):
    current = start
    frontier = []
    explored = []   #might not be necessary
    while True:
        if current == goal: 
            # do I print the optimal solution? call a function for that?
            explored.append(current)
            break
        explored.append(current)
        for node in tree[current]:
            frontier.append(node)
        if len(frontier) == 0:
            return '\0'
        current = frontier.pop(0)
    return explored

def main():
    explored = BFS(initial_state,goal_state)
    if explored != '\0':
        for node in explored:
            print(node)
    else:
        raise Exception("Goal state not found")
    
    
if __name__ == "__main__":
    main()

