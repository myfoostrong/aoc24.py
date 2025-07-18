import sys
import os
from requests import get

SESS = os.environ["SESS"]

def fetch(day):
    cookies = {"session": SESS}
    r = get(f"https://adventofcode.com/2024/day/{day}/input", cookies=cookies)
    with open(f"./input/{day}.txt", "w") as f:
        f.write(r.text)

if __name__ == "__main__":
    day = sys.argv[1]
    fetch(day)
