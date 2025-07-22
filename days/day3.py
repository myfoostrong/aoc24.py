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
            instr = []
            dont_iter = re.finditer("don\'t\(\)", line)
            do_iter = re.finditer("do\(\)", line)
            start = 0
            for dont in dont_iter:
                end = dont.span()[0]
                if start > end:
                    continue
                instr.append((start,end))
                try:
                    do = next(do_iter)
                except StopIteration:
                    break
                while do.span()[0] < end:
                    try:
                        do = next(do_iter)
                    except StopIteration:
                        break
                start = do.span()[0]
                
            for cut in instr:
                clip = line[cut[0]:cut[1]]
                x = re.findall("mul\(([0-9]*),([0-9]*)\)", clip)
                for pair in x:
                    safe_reports += (int(pair[0]) * int(pair[1]))
    return safe_reports
