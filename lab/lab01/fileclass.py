#Nicholas Smith

import sys
import re

def ret(word):
  return word[20:]

def rot(numb):
  return int(numb[:20])

class census:
    def __init__(self, filename):
        self.sorted = []
        with open(filename, 'r') as fileObject:
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
            self.sorted = census_list
            #for x in census_list:
            #    print(x)

    def display(self):
        """Displays the contents of the .dp file"""
        for x in self.sorted:
            print(x)
        return
    
    def searchByNum(self, number):
        """Searches for the district and number pair"""
        for x in self.sorted:
            match = re.search(str(number), x)
            if match:
                print(x)
                return
     
    def searchByDistrict(self, district):
       """Searches for the number and district pair."""
       for x in self.sorted:
            match = re.search(district, x)
            if match:
                print(x)
                return
    
#x = census("mdgeo2010.dp")
#x.display()
#print('\n')
#x.searchByNum(60463)
#x.searchByDistrict("Worton CDP")
