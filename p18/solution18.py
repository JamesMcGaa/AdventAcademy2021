import math

class Leaf:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.rigth = None
    
    def toArray(self):
        return self.value
    
    def explode(self):
        return False
    
    def split(self):
        if self.value > 10:
            values = [self.value // 2, int(math.ceil(self.value / 2))]
            replacement = SnailfishNumber(values, self.parent, self.parent.depth + 1)
            if self.parent.right == self:
                self.parent.right = replacement
            else:
                self.parent.left = replacement
            return True
        
        return False
    

class SnailfishNumber:
    def __init__(self, inp, parent = None, depth = 0):
        self.left = snailfishOrRegular(inp[0], self, depth + 1)
        self.right = snailfishOrRegular(inp[1], self, depth + 1)
        self.parent = parent
        self.depth = depth
    
    def toArray(self):
        return [self.left.toArray(), self.right.toArray()]
    
    def next_right_leaf(self, val):
        current = self
        while current.parent != None and current.parent.right == current:
            current = current.parent
        
        if current.parent != None:
            current = current.parent.right
        else:
            return None

        while type(current) != Leaf:
            current = current.left
        
        current.value += val
        return current.value

    def next_left_leaf(self, val):
        current = self
        while current.parent != None and current.parent.left == current:
            current = current.parent
        
        if current.parent != None:
            current = current.parent.left
        else:
            return None

        while type(current) != Leaf:
            current = current.right
        
        current.value += val    
        return current.value

    def explode(self):
        if self.depth == 4:
            self.next_right_leaf(self.right.value)
            self.next_left_leaf(self.left.value)
            if self.parent.right == self:
                self.parent.right = Leaf(0, self.parent)
            else:
                self.parent.left = Leaf(0, self.parent)
            return True
        else:
            return self.left.explode() or self.right.explode()
    
    def split(self):
        return self.left.split() or self.right.split()


def snailfishOrRegular(inp, parent, depth):
    if type(inp) == list:
        return SnailfishNumber(inp, parent, depth)

    return Leaf(inp, parent)



inpt = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
root = SnailfishNumber(inpt)
# root = SnailfishNumber([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])
print(root.toArray())
root.explode()
print(root.toArray())