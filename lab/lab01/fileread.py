#Nicholas Smith

import sys
import re

def ret(word):
  return word[20:]

def rot(numb):
  return int(numb[:20])
  
with open(sys.argv[1], 'r') as fileObject:
  census_list = []
  fileData = fileObject.readlines()
  for line in fileData:
    match = re.search(r'(\d+)', line[213:300])  # Find the initial sequence of numbers
    if match:
        numbers = match.group(1)
        rest = line[226:300]  # Extract the remaining part
    else:
        numbers = ""  # No numbers found
        rest = line[213:300]   
    census_list.append(numbers.ljust(20) + rest)
  census_list.sort(key=rot)
  census_list.sort(key=ret)
  for x in census_list:
    print(x)

