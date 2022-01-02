import math
import ast
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
            replacement = SnailfishNumber(values, None, None, self.parent)
            if self.parent.right == self:
                self.parent.right = replacement
            else:
                self.parent.left = replacement
            return True
        
        return False
    

class SnailfishNumber:
    def __init__(self, inp, additionLeft, additionRight, parent = None):
        if inp != None:
            self.left = snailfishOrRegular(inp[0], self)
            self.right = snailfishOrRegular(inp[1], self)
            self.parent = parent
        else:
            self.left = additionLeft
            self.left.parent = self
            self.right = additionRight
            self.right.parent = self
            self.parent = None
    
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
        if self.depth() == 4:
            self.next_right_leaf(self.right.value)
            self.next_left_leaf(self.left.value)
            if self.parent.right == self:
                self.parent.right = Leaf(0, self.parent)
            else:
                self.parent.left = Leaf(0, self.parent)
            return True
        else:
            return self.left.explode() or self.right.explode()
    
    def depth(self):
        current = self
        depth = 0
        while current.parent != None:
            depth += 1
            current = current.parent
        return depth
    
    def split(self):
        return self.left.split() or self.right.split()


def snailfishOrRegular(inp, parent):
    if type(inp) == list:
        return SnailfishNumber(inp, None, None, parent)

    return Leaf(inp, parent)



# inpt = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
# root = SnailfishNumber(inpt, None, None)
# # root = SnailfishNumber([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])
# print(root.toArray())
# root.explode()
# print(root.toArray())


f = open("input18_test.txt", "r")
input_raw = [ast.literal_eval(line.strip()) for line in f.readlines()]
expression1 = SnailfishNumber(input_raw[0], None, None)
for expression2 in input_raw[1:]:
    expression2 = SnailfishNumber(expression2, None, None)
    expression1 = SnailfishNumber(None, expression1, expression2)
    while True:
        if expression1.explode():
            continue
        if expression1.split():
            continue
        break
    expression1.explode()
print(expression1.toArray())