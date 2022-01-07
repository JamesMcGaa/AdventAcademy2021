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
        
    
    def get_neighbors(self, printable = False):
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
                # print(set([HORIZONTAL_TO_LEGAL[tower_idx], "."]), set(self.towers[tower_idx]))
                exists_space = set(self.towers[tower_idx]) == set([HORIZONTAL_TO_LEGAL[tower_idx], "."]) or set(self.towers[tower_idx]) == set(".")


                open_path = True
                #make sure everything in between is clear
                for other_hallway_idx, other_hallway_val in self.hallways.items():
                    low = min(hallway_idx, tower_idx)
                    hi = max(hallway_idx, tower_idx)
                    if other_hallway_idx != hallway_idx and low <= other_hallway_idx and other_hallway_idx <= hi and other_hallway_val != ".":
                        open_path = False
                        break

                if exists_space and open_path:
                    tower_height = 3
                    while self.towers[tower_idx][tower_height] == HORIZONTAL_TO_LEGAL[tower_idx]:
                        tower_height -= 1
                    if printable:
                        print(tower_height)
                    new_hallways = copy.deepcopy(self.hallways)
                    new_towers = copy.deepcopy(self.towers)
                    new_hallways[hallway_idx] = "."
                    new_towers[tower_idx][tower_height] = hallway_value

                    neighbors.append(
                        (State(new_towers, new_hallways), (abs(hallway_idx - tower_idx) + tower_height + 1) * VALUE_TO_COST[hallway_value])
                    )

        return neighbors 

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

L2 = State(
                {
                    3: ["B", "D", "D", "A"],
                    5: ["C", "C", "B", "D"],
                    7: ["B", "B", "A", "C"],
                    9: [".", "A", "C", "A"],
                },
                {
                    1: ".",
                    2: ".",
                    4: ".",
                    6: ".",
                    8: ".",
                    10: ".",
                    11: "D",
                },
            )

L4 = State(
                {
                    3: ["B", "D", "D", "A"],
                    5: ["C", "C", "B", "D"],
                    7: [".", "B", "A", "C"],
                    9: [".", ".", "C", "A"],
                },
                {
                    1: "A",
                    2: ".",
                    4: ".",
                    6: ".",
                    8: ".",
                    10: "B",
                    11: "D",
                },
            )
L5 = State(
                {
                    3: ["B", "D", "D", "A"],
                    5: ["C", "C", "B", "D"],
                    7: [".", ".", "A", "C"],
                    9: [".", ".", "C", "A"],
                },
                {
                    1: "A",
                    2: ".",
                    4: ".",
                    6: ".",
                    8: "B",
                    10: "B",
                    11: "D",
                },
            )
L6 = State(
                {
                    3: ["B", "D", "D", "A"],
                    5: ["C", "C", "B", "D"],
                    7: [".", ".", ".", "C"],
                    9: [".", ".", "C", "A"],
                },
                {
                    1: "A",
                    2: "A",
                    4: ".",
                    6: ".",
                    8: "B",
                    10: "B",
                    11: "D",
                },
            )
L7a = State(
                {
                    3: ["B", "D", "D", "A"],
                    5: [".", "C", "B", "D"],
                    7: [".", ".", ".", "C"],
                    9: [".", ".", "C", "A"],
                },
                {
                    1: "A",
                    2: "A",
                    4: ".",
                    6: "C",
                    8: "B",
                    10: "B",
                    11: "D",
                },
            )
L7 = State(
                {
                    3: ["B", "D", "D", "A"],
                    5: [".", "C", "B", "D"],
                    7: [".", ".", "C", "C"],
                    9: [".", ".", "C", "A"],
                },
                {
                    1: "A",
                    2: "A",
                    4: ".",
                    6: ".",
                    8: "B",
                    10: "B",
                    11: "D",
                },
            )
L8 = State(
                {
                    3: ["B", "D", "D", "A"],
                    5: [".", ".", "B", "D"],
                    7: [".", "C", "C", "C"],
                    9: [".", ".", "C", "A"],
                },
                {
                    1: "A",
                    2: "A",
                    4: ".",
                    6: ".",
                    8: "B",
                    10: "B",
                    11: "D",
                },
            )
L10 = State(
                {
                    3: ["B", "D", "D", "A"],
                    5: [".", ".", ".", "."],
                    7: [".", "C", "C", "C"],
                    9: [".", ".", "C", "A"],
                },
                {
                    1: "A",
                    2: "A",
                    4: "D",
                    6: "B",
                    8: "B",
                    10: "B",
                    11: "D",
                },
            )
L11 = State(
                {
                    3: ["B", "D", "D", "A"],
                    5: [".", ".", ".", "B"],
                    7: [".", "C", "C", "C"],
                    9: [".", ".", "C", "A"],
                },
                {
                    1: "A",
                    2: "A",
                    4: "D",
                    6: ".",
                    8: "B",
                    10: "B",
                    11: "D",
                },
            )
L12 = State(
                {
                    3: ["B", "D", "D", "A"],
                    5: [".", ".", "B", "B"],
                    7: [".", "C", "C", "C"],
                    9: [".", ".", "C", "A"],
                },
                {
                    1: "A",
                    2: "A",
                    4: "D",
                    6: ".",
                    8: ".",
                    10: "B",
                    11: "D",
                },
            )
L13 = State(
                {
                    3: ["B", "D", "D", "A"],
                    5: [".", "B", "B", "B"],
                    7: [".", "C", "C", "C"],
                    9: [".", ".", "C", "A"],
                },
                {
                    1: "A",
                    2: "A",
                    4: "D",
                    6: ".",
                    8: ".",
                    10: ".",
                    11: "D",
                },
            )
L15 = State(
                {
                    3: ["B", "D", "D", "A"],
                    5: [".", "B", "B", "B"],
                    7: ["C", "C", "C", "C"],
                    9: [".", ".", ".", "."],
                },
                {
                    1: "A",
                    2: "A",
                    4: "D",
                    6: ".",
                    8: ".",
                    10: "A",
                    11: "D",
                },
            )


START_INPUT = State(
                        {
                            3: ["D", "D", "D", "B"],
                            5: ["B", "C", "B", "D"],
                            7: ["A", "B", "A", "A"],
                            9: ["C", "A", "C", "C"],
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
graph = Graph()
        
from collections import deque
q = deque()
q.append(START_INPUT)
seen = set()
seen.add(START_INPUT.to_string())

while len(q) > 0: 
    current = q.popleft()
    neighbors = current.get_neighbors()
    for neighbor, dist in neighbors:
        new_state_str = neighbor.to_string()
        graph.add_edge(current.to_string(), new_state_str, dist)
        if new_state_str not in seen:
            seen.add(new_state_str)
            q.append(neighbor)

print(find_path(graph, START_INPUT.to_string(), END.to_string()))