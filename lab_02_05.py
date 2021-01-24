from itertools import permutations

s = input()
for permutation in set(permutations(s)):
    print (''.join(permutation))