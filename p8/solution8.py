import os 

f = open("input8_test.txt", "r")
input_cast = [[group.split() for group in line.split("|")] for line in  f.readlines()]
from itertools import permutations
print(input_cast)

# part a
counter = 0
for line in input_cast:
    post = line[1]
    for seq in post:
        if len(seq) in [2,3,4,7]:
            counter += 1
print(counter)

ALPHABET = 'abcdefg'
# part b
def solve(pre, post):
    raw_to_true_mapping = {letter:set(ALPHABET) for letter in ALPHABET}

    for seq in pre: #1
        if len(seq) == 2:
            for letter in seq:
                raw_to_true_mapping[letter] = raw_to_true_mapping[letter] & set('cf')

    for seq in pre: #7s
        if len(seq) == 3:
            for letter in seq:
                raw_to_true_mapping[letter] = raw_to_true_mapping[letter] & set('acf')

    for seq in pre: #4s
        if len(seq) == 4:
            for letter in seq:
                raw_to_true_mapping[letter] = raw_to_true_mapping[letter] & set('bcdf')

    for seq in pre: #2,3,5
        if len(seq) == 5:
            for letter in seq:
                raw_to_true_mapping[letter] = raw_to_true_mapping[letter] & set('bcdf')

    for seq in pre: #0,6,9
        if len(seq) == 6:
            for letter in seq:
                raw_to_true_mapping[letter] = raw_to_true_mapping[letter] & set('bcdf')
    
    # nothing learned from 8s 
    
    mapping = {}
    perms = [''.join(p) for p in permutations(ALPHABET)]
    for perf2 in perms:
        for perm in perms:
            good = True
            for i in range(len(ALPHABET)):
                true = ALPHABET[i]
                proposed = perm[i]
                if not true in raw_to_true_mapping[proposed]:
                    good = False
                    break
            
            if good:
                for i in range(len(ALPHABET)):
                    mapping[ALPHABET[i]] = perm[i]
                break
    print(mapping)
        
    # true_to_raw_mapping = {letter:set() for letter in 'abcdefg'}
    # for true in 'abcdefg':
    #     for raw, possible_trues in raw_to_true_mapping.items():
    #         if true in possible_trues:
    #             true_to_raw_mapping[true].add(raw)


        
    

    

    
    for line in raw_to_true_mapping:
        print(line, raw_to_true_mapping[line])

    # for line in true_to_raw_mapping:
    #     print(line, true_to_raw_mapping[line])

def solved(mapping):
    return all([len(mapping[key]) == 1 for key in mapping])


for line in input_cast[:1]:
    pre, post = line
    solve(pre, post)