#!/bin/python3
from itertools import combinations
from functools import reduce


# Puzzle 1
# Step by step
with open('input.txt') as f:
	adapters = sorted([int(line[:-1]) for line in f])
	jolts = [0] + adapters + [adapters[-1] + 3]
	diff = [j - jolts[n] for n,j in enumerate(jolts[1:])]

	print(diff.count(1) * diff.count(3))

# As one-liner
with open('input.txt') as f: print((lambda adapters: (lambda jolts: (lambda diff: diff.count(1) * diff.count(3))([j - jolts[n] for n,j in enumerate(jolts[1:])]))([0] + adapters + [adapters[-1] + 3]))(sorted([int(line[:-1]) for line in f])))


# Puzzle 2
# Step by step
def is_valid(jolts):
        return all([(j - jolts[n] <= 3) for n,j in enumerate(jolts[1:])])

def num_pair_opts(p_opts_i):
        opts_i = p_opts_i[1]
        n = 1 if is_valid(p_opts_i[0]) else 0
        for c in (cmb for _n in range(len(opts_i)) for cmb in combinations(opts_i, _n + 1)):
                if is_valid(sorted(list(p_opts_i[0]) + list(c))): n+=1
        return n

with open('input.txt') as f:
	adapters = sorted([int(line[:-1]) for line in f])
	jolts = [0] + adapters + [adapters[-1] + 3]
	jd = [(0,)] + [(j, j - jolts[n]) for n,j in enumerate(jolts[1:])]
	fixed = [j[0] for n,j in enumerate(jd) if (n == 0) or (j[1] == 3) or (jd[n + 1][1] == 3)]
	pairs = [(fixed[n], f) for n,f in enumerate(fixed[1:])]
	p_opts = [(p, [j for j in jolts if p[0] < j < p[1]]) for p in pairs]

	print(reduce(lambda x,y: x*y, [num_pair_opts(p_opts_i) for p_opts_i in p_opts]))

# As one-liner
# num_pair_opts function
#def num_pair_opts(p_opts_i):
#        return sum([1 if is_valid(p_opts_i[0]) else 0] + [1 for c in (cmb for _n in range(len(p_opts_i[1])) for cmb in combinations(p_opts_i[1], _n + 1)) if is_valid(sorted(list(p_opts_i[0]) + list(c)))])

with open('input.txt') as f: print((lambda adapters,num_pair_opts: (lambda jolts: (lambda jd: (lambda fixed: (lambda pairs: (lambda p_opts: reduce(lambda x,y: x*y, [num_pair_opts(p_opts_i) for p_opts_i in p_opts]))([(p, [j for j in jolts if p[0] < j < p[1]]) for p in pairs]))([(fixed[n], f) for n,f in enumerate(fixed[1:])]))([j[0] for n,j in enumerate(jd) if (n == 0) or (j[1] == 3) or (jd[n + 1][1] == 3)]))([(0,)] + [(j, j - jolts[n]) for n,j in enumerate(jolts[1:])]))([0] + adapters + [adapters[-1] + 3]))(sorted([int(line[:-1]) for line in f]), lambda p_opts_i,is_valid=(lambda jolts:all([(j - jolts[n] <= 3) for n,j in enumerate(jolts[1:])])): sum([1 if is_valid(p_opts_i[0]) else 0] + [1 for c in (cmb for _n in range(len(p_opts_i[1])) for cmb in combinations(p_opts_i[1], _n + 1)) if is_valid(sorted(list(p_opts_i[0]) + list(c)))])))
