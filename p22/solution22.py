

class Cube:
    def __init__(self, line):
        operation, remainder = line.split()
        sections = remainder.split(",")
        self.operation = operation
        self.x = [int(num) for num in sections[0].split("=")[1].split("..")]
        self.y = [int(num) for num in sections[0].split("=")[1].split("..")]
        self.z = [int(num) for num in sections[0].split("=")[1].split("..")]
    
    def intersection(self, other_cube):
        largest_min = max(min(self.x))


f = open("input22_test.txt", "r")
cubes = [Cube(line.strip()) for line in f.readlines()]
active = set()
for cube in cubes:
    