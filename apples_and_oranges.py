"""
Solution for
Hackerrank problem: https://www.hackerrank.com/challenges/apple-and-orange/problem
"""
import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    returns the count of apples and oranges in the specified area. 
    """
    appleCount = 0
    orangeCount = 0
    #loop through elements of apples 
    for x in apples:
        #each time add element to a
        distance = a+x
        if distance >= s and distance <= t:
            appleCount+=1
    
    #same as apples for oranges
    for y in oranges:
        distance = b+y
        if distance >= s and distance <= t:
            orangeCount+=1
    
    #print the results 
    print(appleCount)
    print(orangeCount)
     

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
