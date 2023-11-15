class Node:
    def __init__(self, n, uv = None):
        self.neighbors = n
        self.utility_value = uv

tree = {
    'A':Node(['B','C']),
    'B':Node([],5),
    'C':Node(['D','E']),
    'D':Node(['F','G']),
    'E':Node(['H','I']),
    'F':Node([],1),
    'G':Node(['J','K']),
    'H':Node([],5),
    'I':Node(['L','M']),
    'J':Node([],4),
    'K':Node([],2),
    'L':Node([],4),
    'M':Node([],3)
}

current_state = tree['A']

def max_turn(t, state):
    current_max_node = t[state.neighbors[0]]
    neighbor = current_max_node
    #neighbor_name refers to the letter assigned to each node
    if neighbor.utility_value == None:
        neighbor.utility_value = min_turn(t,neighbor)
        
    for i in range(1,len(state.neighbors)):
        neighbor = t[state.neighbors[i]]
        if neighbor.utility_value == None:
            neighbor.utility_value = min_turn(t,neighbor)
        
        if neighbor.utility_value >= current_max_node.utility_value: current_max_node = neighbor
    
    return current_max_node.utility_value

def min_turn(t, state):
    current_min_node = t[state.neighbors[0]]
    neighbor = current_min_node
    #neighbor_name refers to the letter assigned to each node
    if neighbor.utility_value == None:
        neighbor.utility_value = min_turn(t,neighbor)
        
    for i in range(1,len(state.neighbors)):
        neighbor = t[state.neighbors[i]]
        if neighbor.utility_value == None:
            neighbor.utility_value = min_turn(t,neighbor)
        
        if neighbor.utility_value >= current_min_node.utility_value: current_min_node = neighbor
    
    return current_min_node.utility_value

def minimax(t, cur_state,MAX):
    if(MAX == True):
        return max_turn(tree,cur_state)
    else:
        return min_turn(tree,cur_state)

def main():
    result = minimax(tree, current_state, True)
    print("The utility value of the initial state is ",result)
    
    
if __name__ == "__main__":
    main()