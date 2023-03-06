#!/usr/bin/env python3

import sys

Fsum = 0
countSum = 0

for line in sys.stdin:
    line = line.strip().split()
    m = int(line[0])
    count = int(line[1])

    Fsum += m*count
    countSum += count

print(Fsum/countSum)