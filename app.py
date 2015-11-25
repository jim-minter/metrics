#!/usr/bin/python

import os
import sys
import time


def use_cpu(pc, s):
    s1 = time.time()
    while time.time() < s1 + s:
        s2 = time.time()
        while time.time() < s2 + 0.1 * pc:
            pass

        target = s2 + 0.1 - time.time()
        if target > 0:
            time.sleep(target)


data = []
def use_mem(pc):
    target = int(100 * pc)

    while len(data) < target:
        data.append("\0" * int(pc * maxmem * 2**20 / 100))
    while len(data) > target:
        data.pop()


def triangle():
    while True:
        for i in range(10):
            yield i / 10.0
        for i in range(10, 0, -1):
            yield i / 10.0


maxmem = int(os.environ.get("MAXMEM", "100"))
interval = int(os.environ.get("INTERVAL", "5"))
for p in triangle():
    print >>sys.stderr, "%s: using %0.0f%% CPU and memory" % \
        (time.ctime(), 100 * p)
    use_mem(p)
    use_cpu(p, interval)
