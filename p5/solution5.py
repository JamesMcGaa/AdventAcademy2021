import os 
f = open("input5_test.txt", "r")
input_cast = [line.split("->") for line in  f.readlines()]

global_counts = {}

class Line:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d 
        self.orientation = "vert" if a == c else "horz"
    
    def intersects(self, other):
        if self.orientation == "vert" and other.orientation == "vert" and a == c:
            start, end = difference_formula(self.b, self.d, other.b, other.d)
            if start is not None:
                for i in range(start, end+1):
                    global_counts.add((a,i))
        
        if self.orientation == "horz" and other.orientation == "horz" and b == d:
            start, end = difference_formula(self.a, self.c, other.a, other.c)
            if start is not None:
                for i in range(start, end+1):
                    global_counts.add((i,b))

def difference_formula(x1, x2, y1, y2):
    max_x = max(x1,x2)
    max_y = max(y1,y2)
    min_x = min(x1,x2)
    min_y = min(y1,y2)

    small_max = min(max_x, max_y)
    large_min = max(min_x, min_y)

    return (large_min, small_max) if small_max > large_min else (None, None)

# vertical_parallels = {}
# horizontal_parallels = {}

lines = []
for line in input_cast:
    a, b = line[0].split(",")
    c, d = line[1].split(",")
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    if a == c or b == d:
        new_line = Line(a,b,c,d)
        for line in lines:
            new_line.intersects(line)
        lines.append(new_line)
print(len(global_counts))
print(global_counts)
    # if a == c: 
    #     if a not in vertical_parallels:
    #         vertical_parallels[a] = set()
    #     vertical_parallels[a].add(Line(a,b,c,d))

    # if b == d: 
    #     if b not in horizontal_parallels:
    #         horizontal_parallels[b] = set()
    #     horizontal_parallels[b].add(Line(a,b,c,d))
            
        


