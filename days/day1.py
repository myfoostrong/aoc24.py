import os
import bisect

def part1():
    distances = []
    left = []
    right = []
    with open("./input/1.txt") as f:
        for line in f:
            vals = line.split("   ")
            bisect.insort(left, int(vals[0]))
            bisect.insort(right, int(vals[1]))
    for i, l in enumerate(left):
        distances.append(abs(l - right[i]))
    return sum(distances)


def part2():
    left = []
    sim_score = 0
    counts = {}
    with open("./input/1.txt") as f:
        for line in f:
            vals = list(map(lambda x: int(x), line.split("   ")))
            left.append(vals[0])
            if counts.get(vals[1]) is None:
                counts[vals[1]] = 1
            else:
                counts[vals[1]] += 1
    for l in left:
        count = counts.get(l)
        if count is None:
            count = 0
        sim_score += l * count
    return sim_score
            

