import numpy as np 
import pprint
from itertools import permutations
import math

x = np.array([[ 1, 0, 0],
  [ 0, 1, 0],
  [ 0, 0, 1]])
all_perms = [np.array(perm) for perm in permutations(x)]
valid_perms = []
for permutation in all_perms:
    for x in [-1, 1]:
        for y in [-1, 1]:
            for z in [-1, 1]:
                perm_copy = permutation.copy()
                perm_copy[0,:] *= x
                perm_copy[1,:] *= y
                perm_copy[2,:] *= z
                # if int(np.linalg.det(perm_copy)) == 1:
                valid_perms.append(perm_copy)

absolute_points = [] 
def absolute_point_to_pairwise_dists_with_other_abs(abs):
    dists = []
    for point in absolute_points:
        if not np.array_equal(point, abs):
            l2 = 0
            for i in range(3):
                l2 += (point[i] - abs[i]) ** 2
            dists.append(l2)
    return dists

class Scan:
    def __init__(self, data, is_scan_0=False):
        self.data = data
        self.proper_data = data if is_scan_0 else False
        self.perms = self.list_full_permutations()
    
    def list_full_permutations(self):
        results = []
        for perm in valid_perms:
            results.append(np.matrix(np.matmul(self.data, perm)))
        return results
    


f = open("input19_test.txt", "r")
lines = [line.strip() for line in f.readlines()]

data = None
scans = []
for line in lines:
    if line == "":
        scans.append(Scan(data))
        data = None

    else:
        if data == None:
            data = []
        data.append([int(coord) for coord in line.split(',')])
scans.append(Scan(data))

for abs in scans[0].data:
    absolute_points.append(abs)


def solve_scan(scan):
    for perm in scan.list_full_permutations():
        # number_of_points_with_abs_match = 0 #note this is always the same val for each point
        print("---------------------------------------")
        offsets = []
        for point in perm:
            dists = []
            for other in perm:
                if not np.array_equal(point, other):
                    l2 = 0
                    for i in range(3):
                        l2 += (point[0,i] - other[0,i]) ** 2
                    dists.append(l2)

            #lets see if this point is in abs
            for abs in absolute_points:
                abs_dists = absolute_point_to_pairwise_dists_with_other_abs(abs)
                if len(set(abs_dists) & set(dists)) >= 11: #not every point is already in abs
                    offsets.append(abs - point)
                
        if len(offsets) > 0:
            uneven = False
            for offset in offsets:
                if not np.array_equal(offsets[0], offset):
                    uneven = True
            
            if not uneven:
                true_offset_for_this_scan = offsets[0]
                
                for point in perm: 
                    if all([not np.array_equal(point + true_offset_for_this_scan, other) for other in abs]):
                        absolute_points.append(point)

for scan in scans[1:]:
    solve_scan(scan)