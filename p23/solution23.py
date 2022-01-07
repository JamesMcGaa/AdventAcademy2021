from dijkstar import Graph, find_path
import random
import time
# MOVES = {
#     1: [2],
#     2: [1, 3, 5],
#     3: [2, 4, 5],
#     4: [3],
#     5: [2, 3, 6, 8],
#     6: [5, 7, 8],
#     7: [6],
#     8: [5, 6, 9, 11],
#     9: [8, 10, 11],
#     10: [9],
#     11: [8, 9, 12, 14],
#     12: [11, 13, 14],
#     13: [12],
#     14: [11, 12, 15],
#     15: [14],
# }
# WEIGHTS = {
#     "A" : 1,
#     "B" : 10,
#     "C" : 100,
#     "D" : 1000,
# }
# class State():
#     def __init__(self, init_string, init_positions):
#         if init_string is not None:
#             self.positions = {i+1:char for i, char in enumerate(init_string)}
#         else:
#             self.positions = init_positions
    
#     def to_string(self):
#         st = ""
#         for ind in range(1, 16):
#             st += self.positions[ind]
#         return st
    
#     def get_neighbors(self, graph, seen):
#         neighbors = []
#         for position, char in self.positions.items():
#             for end_position in MOVES[position]:
#                 if self.positions[end_position] == "." and char != ".":
#                     match end_position: #improper enter top stack, except exiting bottom stack 
#                         case 3:
#                             if (char != "A" and position != 4): # or (char == "A" and position == 4):
#                                 continue
#                         case 6:
#                             if (char != "B" and position != 7): # or (char == "B" and position == 7):
#                                 continue
#                         case 9:
#                             if (char != "C" and position != 10): # or (char == "C" and position == 10):
#                                 continue
#                         case 12:
#                              if (char != "D" and position != 13): # or (char == "D" and position == 13):
#                                 continue
#                         case _: 
#                             pass
                    
#                     multiplier = 1 if (end_position in [1,4,7,10,13,15] or position in [1,4,7,10,13,15]) else 2

#                     new_dict = self.positions.copy()
#                     new_dict[end_position] = new_dict[position]
#                     new_dict[position] = "."
#                     new_state = State(None, new_dict)
#                     new_state_str = new_state.to_string()
#                     if new_state_str not in seen:
#                         seen.add(new_state_str)
#                         neighbors.append(new_state)
#                     graph.add_edge(self.to_string(), new_state_str, multiplier * WEIGHTS[self.positions[position]])
#         return neighbors    
                        
# graph = Graph()
# START_EXAMPLE =  "..BA.CD.BC.DA.."
# START = "..DB.BD.AA.CC.."
# END ="..AA.BB.CC.DD.."
# stack = [State(START, None)]
# seen = set()
# seen.add(stack[0].to_string())
# while len(stack) > 0:
#     current = stack.pop()
    
#     neighbors = current.get_neighbors(graph, seen)
#     for neighbor in neighbors:
#         stack.append(neighbor)
# print(find_path(graph, START, END))


# MOVES = {
#     1: [2],
#     2: [1, 3, 7],
#     3: [2, 4, 7],
#     4: [3, 5],
#     5: [4, 6],
#     6: [5],
#     7: [2, 3, 8, 12],
#     8: [7, 9, 12],
#     9: [8, 10],
#     10: [9, 11],
#     11: [10],
#     12: [7, 8, 13, 17],
#     13: [12, 14, 17],
#     14: [13, 15],
#     15: [14, 16],
#     16: [15],
#     17: [12, 13, 18, 22],
#     18: [17, 19, 22],
#     19: [18, 20],
#     20: [19, 21],
#     21: [20],
#     22: [17, 18, 23],
#     23: [22],
# }


# start: list of [end, weight_multiplier, [need to be clears]]
MOVES = {
    1: [
        [3, 3, [2, 3]],
        [8, 5, [2, 7, 8]],
        [13, 7, [2, 7, 12, 13]],
        [18, 9, [2, 7, 12, 17, 18]],
    ],
    2: [
        [3, 2, [3]],
        [8, 4, [7, 8]],
        [13, 6, [7, 12, 13]],
        [18, 8, [7, 12, 17, 18]],
    ],
    7: [
        [3, 2, [3]],
        [8, 2, [8]],
        [13, 4, [12, 13]],
        [18, 6, [12, 17, 18]],
    ],
    12: [
        [3, 4, [7, 3]],
        [8, 2, [8]],
        [13, 2, [13]],
        [18, 4, [17, 18]],
    ],
    17: [
        [3, 6, [12, 7, 3]],
        [8, 4, [12, 8]],
        [13, 2, [13]],
        [18, 2, [18]],
    ],
    22: [
        [3, 8, [17, 12, 7, 3]],
        [8, 6, [17, 12, 8]],
        [13, 4, [17, 13]],
        [18, 2, [18]],
    ],
    23: [
        [3, 9, [23, 17, 12, 7, 3]],
        [8, 7, [23, 17, 12, 8]],
        [13, 5, [23, 17, 13]],
        [18, 3, [23, 18]],
    ],
}

HALLWAY_KEYS = list(MOVES.keys())
for TOP_STACK in [3,8,13,18]:
    MOVES[TOP_STACK] = [
        [TOP_STACK + 1, 1, [TOP_STACK + 1]]
    ]

    for HALLWAY in HALLWAY_KEYS:
        _, multiplier, blocking = list(filter(lambda x: x[0] == TOP_STACK, MOVES[HALLWAY]))[0]
        new_block = blocking.copy()
        new_block.remove(TOP_STACK)
        new_block.append(HALLWAY)
        MOVES[TOP_STACK].append([HALLWAY, multiplier, new_block])

for MID_STACK in [4, 5, 9, 10, 14, 15, 19, 20]: 
    MOVES[MID_STACK] = [
        [MID_STACK - 1, 1, [MID_STACK - 1]],
        [MID_STACK + 1, 1, [MID_STACK + 1]]
    ]

for BOTTOM_STACK in [6, 11, 16, 21]: 
    MOVES[BOTTOM_STACK] = [
        [BOTTOM_STACK - 1, 1, [BOTTOM_STACK - 1]],
    ]


WEIGHTS = {
    "A" : 1,
    "B" : 10,
    "C" : 100,
    "D" : 1000,
}
class State():
    def __init__(self, init_string, init_positions):
        if init_string is not None:
            self.positions = {i+1:char for i, char in enumerate(init_string)}
        else:
            self.positions = init_positions
    
    def to_string(self):
        st = ""
        for ind in range(1, len(MOVES) + 1):
            st += self.positions[ind]
        return st
        
    
    def get_neighbors(self):
        neighbors = []
        for position, char in self.positions.items():
            for end_position, multiplier, blocking_spots in MOVES[position]:
                if char != "." and all([self.positions[blocking_idx] == "." for blocking_idx in blocking_spots]):
                    match end_position: #improper enter top stack, except exiting bottom stack 
                        case 3:
                            if (char != "A" and position != 4): # or (char == "A" and position == 4):
                                continue
                            # if char == "A" and all([self.positions[other] == "." or self.positions[other] == "A"] for other in [end_position + 1, end_position + 2, end_position + 3]):
                            #     new_dict = self.positions.copy()
                            #     new_dict[end_position] = new_dict[position]
                            #     new_dict[position] = "."
                            #     new_state = State(None, new_dict)
                            #     return [(new_state, multiplier * WEIGHTS[self.positions[position]])]
                        case 8:
                            if (char != "B" and position != 9): # or (char == "B" and position == 7):
                                continue
                            # if char == "B" and all([self.positions[other] == "." or self.positions[other] == "B"] for other in [end_position + 1, end_position + 2, end_position + 3]):
                            #     new_dict = self.positions.copy()
                            #     new_dict[end_position] = new_dict[position]
                            #     new_dict[position] = "."
                            #     new_state = State(None, new_dict)
                            #     return [(new_state, multiplier * WEIGHTS[self.positions[position]])]
                        case 13:
                            if (char != "C" and position != 14): # or (char == "C" and position == 10):
                                continue
                            # if char == "C" and all([self.positions[other] == "." or self.positions[other] == "C"] for other in [end_position + 1, end_position + 2, end_position + 3]):
                            #     new_dict = self.positions.copy()
                            #     new_dict[end_position] = new_dict[position]
                            #     new_dict[position] = "."
                            #     new_state = State(None, new_dict)
                            #     return [(new_state, multiplier * WEIGHTS[self.positions[position]])]
                        case 18:
                            if (char != "D" and position != 19): # or (char == "D" and position == 13):
                                continue
                            # if char == "D" and all([self.positions[other] == "." or self.positions[other] == "D"] for other in [end_position + 1, end_position + 2, end_position + 3]):
                            #     new_dict = self.positions.copy()
                            #     new_dict[end_position] = new_dict[position]
                            #     new_dict[position] = "."
                            #     new_state = State(None, new_dict)
                            #     return [(new_state, multiplier * WEIGHTS[self.positions[position]])]
                        case _: 
                            pass
                    #cant rise unless its contaminated (inc self)
                    for end_positions, legal_char in [[[3,4,5], "A"], [[8,9,10], "B"], [[13,14,15], "C"], [[18,19,20], "D"]]:
                        if end_position in end_positions and position == end_position + 1:
                            allowed_to_rise = False
                            i = end_position
                            while i <= end_positions[2] + 1:
                                val = self.positions[i]
                                if val != legal_char and val != ".":
                                    allowed_to_rise = True
                                i += 1
                            if not allowed_to_rise:
                                continue

                    # can fall, unless there is a contaminated squ (inc self)
                    for end_positions, legal_char in [[[6,4,5], "A"], [[11,9,10], "B"], [[16,14,15], "C"], [[21,19,20], "D"]]:
                        if end_position in end_positions and position == end_position - 1:
                            allowed_to_fall = True
                            i = end_position
                            while i <= end_positions[0]:
                                val = self.positions[i]
                                if val != legal_char and val != ".":
                                    allowed_to_fall = False
                                i += 1
                            if not allowed_to_fall: #contaminated value, dont fall
                                continue


                    new_dict = self.positions.copy()
                    new_dict[end_position] = new_dict[position]
                    new_dict[position] = "."
                    new_state = State(None, new_dict)
                    neighbors.append((new_state, multiplier * WEIGHTS[self.positions[position]]))
        return neighbors 


def nw(s):
    return "".join(s.split())

now = time.time()         
graph = Graph()
START_EXAMPLE =  "..BDDA.CCBD.BBAC.DACA.."
END = "..AAAA.BBBB.CCCC.DDDD.."
P0 = "..BDDA.CCBD.BBAC..ACA.D"
P1 = "A.BDDA.CCBD.BBAC...CA.D"
P2 = "A.BDDA.CCBD..BAC...CABD"
P3 = "A.BDDA.CCBD...ACB..CABD"
P4 = nw("AA BDDA . CCBD . ...C B ..CA BD")
P5 = nw("AA BDDA . .CBD C ...C B ..CA BD")
P6 = nw("AA BDDA . .CBD . C..C B ..CA BD")
P7 = nw("AA BDDA . .CBD . .C.C B ..CA BD")
P8 = nw("AA BDDA . .CBD . ..CC B ..CA BD")
# stack = [State(START_EXAMPLE, None)]

from collections import deque
q = deque()
q.append(State(START_EXAMPLE, None))

seen = set()
seen.add(State(START_EXAMPLE, None).to_string())
short_circuit = 1000000
counter = 0
while len(q) > 0: # and counter < short_circuit:
    counter += 1
    current = q.pop()
    neighbors = current.get_neighbors()
    for neighbor, dist in neighbors:
        new_state_str = neighbor.to_string()
        graph.add_edge(current.to_string(), new_state_str, dist)
        if new_state_str not in seen:
            seen.add(new_state_str)
            q.append(neighbor)
print(time.time() - now, counter)
print(find_path(graph, START_EXAMPLE, P0))
print("\n")
print(find_path(graph, START_EXAMPLE, P1))
print("\n")
print(find_path(graph, START_EXAMPLE, P2))
print("\n")
print(find_path(graph, START_EXAMPLE, P3))
print("\n")
print(find_path(graph, START_EXAMPLE, P4))
print("\n")
print(find_path(graph, START_EXAMPLE, P5))
print("\n")
print(find_path(graph, START_EXAMPLE, P6))
print("\n")
print(find_path(graph, START_EXAMPLE, P7))
print("\n")
print(find_path(graph, START_EXAMPLE, P8))
print("\n")
print(find_path(graph, START_EXAMPLE, END))
print(time.time() - now)
