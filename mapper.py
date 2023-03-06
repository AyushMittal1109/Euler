#!/usr/bin/env python3

import sys
import random
for line in sys.stdin:
    line = line.strip().split()
    m = int(line[0])

    ans = {}

    for i in range(m):
        sum = 0
        count = 0
        while sum <= 1 :
            count += 1
            sum += random.uniform(0,1)
        if count in ans.keys():
            ans[count] += 1
        else:
            ans[count] = 1
        
    for key in ans.keys():
        print(key,ans[key])
