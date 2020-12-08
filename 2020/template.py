from utils import aoc_comm
import os
import re
from collections import Counter, defaultdict

# --- update day/ year for each challenge
settings = {
    'day' : 8,
    'year' : 2020,
    'cookie-path' : os.path.realpath('../aoc_cookie.json')
}




def parse_input(inp_content):
    inp_content = inp_content.strip()

    yield None

    
@aoc_comm(settings, level = 1)
def solve_l1(page):
    inp = parse_input(page)

    ans = None
    for ee in inp:
        pass

    return ans # if 'ans' is None answer won't be submitted, else it will submit after confirmation 




@aoc_comm(settings, level = 2)
def solve_l2(page):
    inp = parse_input(page)

    ans = None
    for ee in inp:
        pass

    return ans



def main():
    l1_status = solve_l1()
    print(l1_status)

    #l2_status = solve_l2()
    #print(l2_status)


if __name__ == '__main__':
    main()
