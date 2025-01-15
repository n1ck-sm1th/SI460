#Nicholas Smith

import sys
import re

"Gen AI function to help sort the input data"
def sort_by_letters(my_list):
  """
  Sorts a list of strings based on the alphabetical order of the letters 
  within each string, ignoring any leading numbers.

  Args:
    my_list: The list of strings to be sorted.

  Returns:
    A new list containing the sorted strings.
  """

  def extract_letters(string):
    """
    Extracts the letters from the string by removing any leading numbers and 
    extracting only alphabetic characters.
    """
    match = re.match(r'^\d+\s*(.+)', string) 
    if match:
      return ''.join(c for c in match.group(1) if c.isalpha()) 
    else:
      return ''

  return sorted(my_list, key=extract_letters)
  
  
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
  census_list.sort()
  sorted = sort_by_letters(census_list)
  for x in sorted:
    print(x)

