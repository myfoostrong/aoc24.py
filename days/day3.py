import os
import re

def part1():
    safe_reports = 0
    with open("./input/3.txt") as f:
        for line in f:
            x = re.findall("mul\(([0-9]*),([0-9]*)\)", line)
            for pair in x:
                safe_reports += (int(pair[0]) * int(pair[1]))
    return safe_reports


def part2():
    safe_reports = 0
    with open("./input/3.txt") as f:
        for line in f:
            x = re.findall("mul\(([0-9]*),([0-9]*)\)", line)
    return safe_reports
