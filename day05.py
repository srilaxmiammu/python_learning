#LINK: https://www.hackerrank.com/challenges/py-if-else/problem
#LINK: https://www.hackerrank.com/challenges/write-a-function/problem

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n%2==1:
    print("Weird")
elif 2 <= n<= 5:
    print("Not Weird")
elif 6<= n <= 20:
    print("Weird")
else:
    print("Not Weird")



def is_leap(year):
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    return False       
    
    
    
year = int(input())
print(is_leap(year))