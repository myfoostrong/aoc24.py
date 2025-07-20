import os
import bisect

def part1():
    safe_reports = 0
    with open("./input/2.txt") as f:
        for line in f:
            vals = list(map(lambda x: int(x), line.split(" ")))    
            if check_safe(vals):
                safe_reports +=1
    return safe_reports


def check_safe(vals):
    if len(vals) < 2:
        return True
    go_up = (vals[1] - vals[0]) > 0
    for i, v in enumerate(vals):
        if i == 0:
            continue
        if not check_direction(vals[i-1], v, go_up):
            return False
    return True

def check_direction(prev, curr, go_up):
    diff = curr - prev
    if diff == 0:
        return False
    if abs(diff) < 4:
        if go_up:
            return diff > 0
        else:
            return diff < 0
    else:
        return False


def part2():
    safe_reports = 0
    with open("./input/2.txt") as f:
        for line in f:
            vals = list(map(int, line.split(" ")))
            if check_safe2(vals):
                safe_reports +=1
    return safe_reports
            
def check_safe2(vals):
    if len(vals) < 2:
        return True
    go_up = (vals[1] - vals[0]) > 0
    length = len(vals)
    for i, v in enumerate(vals):
        if i == 0:
            continue
        if not check_direction(vals[i-1], v, go_up):
            if i == length - 1:
                return True
            if i == 1:
                if check_safe(vals[1:]):
                    return True
                if check_safe([vals[0]] + vals[2:]):
                    return True
            if i == 2:
                if check_safe(vals[1:]):
                    return True
            if check_safe(vals[:i]+vals[i+1:]):
                return True
            else:
                if check_safe(vals[:i-1]+vals[i:]):
                    return True
            return False
    return True