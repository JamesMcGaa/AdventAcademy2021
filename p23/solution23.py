from dijkstar import Graph, find_path
import random
import time
import copy

HORIZONTAL_TO_LEGAL = {
    3: "A",
    5: "B",
    7: "C",
    9: "D",
}

VALUE_TO_TOWER_IDX = {
    "A" : 3,
    "B" : 5,
    "C" : 7,
    "D" : 9,
}

VALUE_TO_COST = {
    "A" : 1,
    "B" : 10,
    "C" : 100,
    "D" : 1000,
}

class State():
    def __init__(self, towers, hallways):
        # {
        #     3: ["B", "D", "D", "A"],
        #     5: ["C", "C", "B", "D"],
        #     7: ["B", "B", "A", "C"],
        #     9: ["D", "A", "C", "A"],
        # }
        self.towers = towers


        # {
        #     1: ".",
        #     2: ".",
        #     4: ".",
        #     6: ".",
        #     8: ".",
        #     10: ".",
        #     11: ".",
        # }
        self.hallways = hallways

    
    def to_string(self):
        return str(self.towers) + str(self.hallways)
        
    
    def get_neighbors(self):
        neighbors = []

        #pop from tower to hallway 
        for horzontal, tower_list in self.towers.items():
            
            #find the top nonzero value
            top_nonzero = None
            height = None
            for h, value in enumerate(tower_list):
                if value != ".":
                    top_nonzero = value
                    height = h
                    break
                
            #dont pop from a good stack
            if HORIZONTAL_TO_LEGAL[horzontal] == top_nonzero and \
                all([other_val == HORIZONTAL_TO_LEGAL[horzontal] for other_val in self.towers[horzontal][height:]]):
                continue
            
            if top_nonzero is not None:
                for target_hallway in self.hallways.keys():
                    all_clear = True
                    low = min(target_hallway, horzontal)
                    hi = max(target_hallway, horzontal)

                    #make sure everything in between is clear
                    for other_hallway_idx, other_hallway_val in self.hallways.items():
                        if low <= other_hallway_idx and other_hallway_idx <= hi and other_hallway_val != ".":
                            all_clear = False
                            break
                    
                    if all_clear:
                        new_hallways = copy.deepcopy(self.hallways)
                        new_towers = copy.deepcopy(self.towers)
                        new_hallways[target_hallway] = top_nonzero
                        new_towers[horzontal][height] = "."
                        neighbors.append(
                            (State(new_towers, new_hallways), (abs(target_hallway - horzontal) + height + 1) * VALUE_TO_COST[top_nonzero])
                        )
        
        #push from hallway to tower
        for hallway_idx, hallway_value in self.hallways.items():
            #non . chars
            if hallway_value in VALUE_TO_TOWER_IDX: 
                tower_idx = VALUE_TO_TOWER_IDX[hallway_value]
                exists_space = set(self.towers[tower_idx]) == set([VALUE_TO_TOWER_IDX[hallway_value], "."])
                open_path = True
                #make sure everything in between is clear
                for other_hallway_idx, other_hallway_val in self.hallways.items():
                    low = min(other_hallway_idx, hallway_idx)
                    hi = max(other_hallway_idx, hallway_idx)
                    if low <= other_hallway_idx and other_hallway_idx <= hi and other_hallway_val != ".":
                        open_path = False
                        break
                
                if exists_space and open_path:
                    tower_height = 3
                    while tower_height == VALUE_TO_TOWER_IDX[hallway_value]:
                        tower_height -= 1
                    new_hallways = copy.deepcopy(self.hallways)
                    new_towers = copy.deepcopy(self.towers)
                    new_hallways[hallway_idx] = "."
                    new_towers[tower_idx][tower_height] = hallway_value
                    neighbors.append(
                        (State(new_towers, new_hallways), (abs(target_hallway - horzontal) + height + 1) * VALUE_TO_COST[top_nonzero])
                    )

        return neighbors 


# def nw(s):
#     return "".join(s.split())

now = time.time()         
graph = Graph()
# START_EXAMPLE =  "..BDDA.CCBD.BBAC.DACA.."
# END = "..AAAA.BBBB.CCCC.DDDD.."
# P0 = "..BDDA.CCBD.BBAC..ACA.D"
# P1 = "A.BDDA.CCBD.BBAC...CA.D"
# P2 = "A.BDDA.CCBD..BAC...CABD"
# P3 = "A.BDDA.CCBD...ACB..CABD"
# P4 = nw("AA BDDA . CCBD . ...C B ..CA BD")
# P5 = nw("AA BDDA . .CBD C ...C B ..CA BD")
# P6 = nw("AA BDDA . .CBD . C..C B ..CA BD")
# P7 = nw("AA BDDA . .CBD . .C.C B ..CA BD")
# P8 = nw("AA BDDA . .CBD . ..CC B ..CA BD")
# stack = [State(START_EXAMPLE, None)]

START_EXAMPLE = State(
                        {
                            3: ["B", "D", "D", "A"],
                            5: ["C", "C", "B", "D"],
                            7: ["B", "B", "A", "C"],
                            9: ["D", "A", "C", "A"],
                        },
                        {
                            1: ".",
                            2: ".",
                            4: ".",
                            6: ".",
                            8: ".",
                            10: ".",
                            11: ".",
                        },
                    )

END = State(
                {
                    3: ["A", "A", "A", "A"],
                    5: ["B", "B", "B", "B"],
                    7: ["C", "C", "C", "C"],
                    9: ["D", "D", "D", "D"],
                },
                {
                    1: ".",
                    2: ".",
                    4: ".",
                    6: ".",
                    8: ".",
                    10: ".",
                    11: ".",
                },
            )
        
from collections import deque
q = deque()
q.append(
    State(
        {
            3: ["B", "D", "D", "A"],
            5: ["C", "C", "B", "D"],
            7: ["B", "B", "A", "C"],
            9: ["D", "A", "C", "A"],
        },
        {
            1: ".",
            2: ".",
            4: ".",
            6: ".",
            8: ".",
            10: ".",
            11: ".",
        },
    )
)

seen = set()
seen.add(START_EXAMPLE.to_string())

while len(q) > 0: 
    current = q.popleft()
    neighbors = current.get_neighbors()
    for neighbor, dist in neighbors:
        new_state_str = neighbor.to_string()
        graph.add_edge(current.to_string(), new_state_str, dist)
        if new_state_str not in seen:
            seen.add(new_state_str)
            q.append(neighbor)

