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
BIG_NUMS_TO_TRUES = {
    0:set('abcefg'),
    1:set('cf'),
    2:set('acdeg'),
    3:set('acdfg'),
    4:set('bcdf'),
    5:set('abdfg'),
    6:set('abdefg'),
    7:set('acf'),
    8:set('acbdefg'),
    9:set('abcdfg'),
}
SEQ_LENGTH_TO_BIG_NUMS = {
    2:[1],
    3:[7],
    4:[4],
    5:[2,3,5],
    6:[6,9,0],
    7:[8],
}

def sanity_test_big_number_perm(big_number_perm, pre):
    for seq_ind, big_number in enumerate(big_number_perm):
        seq = pre[seq_ind]
        if not big_number in SEQ_LENGTH_TO_BIG_NUMS[len(seq)]:
            return False
    return True

def alphabet_perm_works(alphabet_perm, raw_to_potential_true):
    for raw_ind, true in enumerate(alphabet_perm):
        raw = ALPHABET[raw_ind]
        if not true in raw_to_potential_true[ALPHABET[raw_ind]]:
            return False

    return True

# part b
def solve(pre, post):
    # seq_length_to_seqs = {length:[] for length in range(2,8)} 

    # for seq in pre: #1
    #     seq_length_to_seqs[len(seq)].append(seq)
    

    big_number_perms = list(permutations([index for index in range(10)])) 
    for big_number_perm in big_number_perms:
        if sanity_test_big_number_perm(big_number_perm, pre):

            raw_to_potential_true = {}
            for seq_index, big_number in enumerate(big_number_perm):
                seq = pre[seq_index]
                for letter in seq: 
                    raw_to_potential_true[letter] = BIG_NUMS_TO_TRUES[big_number]
            
            alphabet_perms = list(permutations([ALPHABET[index] for index in range(len(ALPHABET))]))
            for alphabet_perm in alphabet_perms:
                if alphabet_perm_works(alphabet_perm, raw_to_potential_true):

                    for pre_seq in pre:
                        for letter in pre_seq:
                            if letter not in 
                    for raw_ind, true in enumerate(alphabet_perm):
                        raw = ALPHABET[raw_ind]


                    for post_seq in post:
                        pre_ind = big_number_perm[pre.index(post_seq)]
                        print(pre_ind)
                    
                    # return big_number_perm



        


        
    

# def solved(mapping):
#     return all([len(mapping[key]) == 1 for key in mapping])


for line in input_cast[:1]:
    pre, post = line
    for ind, seq in enumerate(pre):
        pre[ind] = sorted(seq)
    for ind, seq in enumerate(post):
        post[ind] = sorted(seq)

    perm = solve(pre, post)
    # for post_seq in post:
    #     pre_ind = perm[pre.index(post_seq)]
    #     print(pre_ind)