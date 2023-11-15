
    
#I made my graph correspond with the classic mathematical xy axis   

class Coordinates:
    def __init__(self,x_coordinate,y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate
    
    def __eq__(self, other_coordinates):
        return (self.x,self.y) == (other_coordinates.x,other_coordinates.y)

    def __str__(self):
        return(f"x={self.x},y={self.y}")
    
class Maze:
    def __init__(self, list_of_lists):
        self.m = list_of_lists

    def get_point(self,coordinates):
        num_rows = len(self.m)
        num_cols = len(self.m[0])
        y = num_rows-1-coordinates.y
        x = coordinates.x
        if(x in range(0,num_cols)and y in range(0,num_rows)):
            return self.m[y][x]
        else:
            return 'X'

def manhattan_distance_to_G(coordinates):
    return (9-coordinates.x)+(6-coordinates.y)

class Node:
    def __init__(self, coordinates):
        self.location = coordinates
        self.manhattan_distance = manhattan_distance_to_G(coordinates)
    
maze = Maze([
    ['X', '-', '-', '-', '-', '-', '-', '-', '-', 'G'],
    ['X', '-', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '-'],
    ['X', '-', 'X', '-', '-', '-', '-', '-', 'X', '-'],
    ['X', '-', 'X', '-', 'X', 'X', 'X', '-', 'X', '-'],
    ['X', '-', '-', '-', 'X', '-', '-', '-', 'X', '-'],
    ['X', 'X', 'X', '-', 'X', '-', 'X', 'X', 'X', '-'],
    ['S', '-', '-', '-', 'X', '-', '-', '-', '-', '-']
])

start_point = Coordinates(0,0)
goal_point = Coordinates(9,6)

def find_index(node_list, h):
    l = len(node_list)
    if l == 0:
        return 0
    for i in range(l):
        if h <= node_list[i].manhattan_distance:
            return i
    return l

def insert_to_frontier(fr,node):
        index = find_index(fr,node.manhattan_distance)
        fr.insert(index,node)


def get_neighbors(coordinates, state_space):
    neighbors = []
    coordinates1 = Coordinates(coordinates.x+1,coordinates.y)
    if state_space.get_point(coordinates1) !='X':
        neighbors.append(coordinates1)
    coordinates2 = Coordinates(coordinates.x-1,coordinates.y)
    if state_space.get_point(coordinates2)!='X':
        neighbors.append(coordinates2)
    coordinates3 = Coordinates(coordinates.x,coordinates.y+1)
    if state_space.get_point(coordinates3)!='X':
        neighbors.append(coordinates3)
    coordinates4 = Coordinates(coordinates.x,coordinates.y-1)
    if state_space.get_point(coordinates4)!='X':
        neighbors.append(coordinates4)   

    return neighbors

        
def GBFS(start, goal,state_space):
    current = start
    frontier = []
    explored = [] 
    while True:
        if current == goal: 
            explored.append(current)
            break
        explored.append(current)
        neighbors = get_neighbors(current,state_space)
        for n in neighbors:
            if(n in explored):
                continue
            insert_to_frontier(frontier,Node(n))    #creates a Node object with the mahattan distance and passes it inserts it accodingly into the frontier

        if len(frontier) == 0:
            return '\0'
        current = frontier.pop(0).location
    return explored

def main():
    explored = GBFS(start_point, goal_point, maze)
    if explored != '\0':
        for node in explored:
            print(node)
    else:
        raise Exception("Goal state not found")
    
    
if __name__ == "__main__":
    main()