#!/bin/python3
from itertools import combinations, takewhile


# Puzzle 1
# Step by step
with open('input.txt') as f:
	offset = 25
	numbers = [int(line[:-1]) for line in f]

	invalid_numbers = []
	for i,n in enumerate(numbers[offset:]):
		prev_numbers = numbers[i:offset + i]

		if not any(sum(c) == n for c in combinations(prev_numbers, 2)):
			invalid_numbers.append(n)

	print(invalid_numbers[0])

# As one-liner
with open('input.txt') as f: print([[n for i,n in enumerate(numbers[25:]) if not any(sum(c) == n for c in combinations(numbers[i:25 + i], 2))][0] for numbers in [[int(line[:-1]) for line in f]]][0])


# Puzzle 2
# Step by step
with open('input.txt') as f:
	offset = 25
	numbers = [int(line[:-1]) for line in f]

	invalid_numbers = []
	for i,n in enumerate(numbers[offset:]):
		prev_numbers = numbers[i:offset + i]

		if not any(sum(c) == n for c in combinations(prev_numbers, 2)):
			invalid_numbers.append(n)

	invalid_number = invalid_numbers[0]

	weakness = []
	for i in range(len(numbers)):
		for j in range(i + 1, len(numbers)):
			if sum(numbers[i:j]) == invalid_number:
				weakness.append(min(numbers[i:j]) + max(numbers[i:j]))
			elif sum(numbers[i:j]) > invalid_number: break
	print(weakness[0])

# As one-liner
with open('input.txt') as f: print((lambda invalid_number, numbers: [arr[0] for arr in [[max(numbers[i:j]) + min(numbers[i:j]) for j in takewhile(lambda j: sum(numbers[i:j]) <= invalid_number, range(i + 1, len(numbers))) if sum(numbers[i:j]) == invalid_number] for i in range(len(numbers))] if len(arr) > 0][0])(*[[[n, numbers] for i,n in enumerate(numbers[25:]) if not any(sum(c) == n for c in combinations(numbers[i:25 + i], 2))][0] for numbers in [[int(line[:-1]) for line in f]]][0]))
