#Nicholas Smith

import sys
import re

def sort_by_letters(census_list):
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
            
    return sorted(census_list, key=extract_letters)

class census:
    def __init__(self, filename):
        """Initializes the census class"""
        self.filename = filename
        self.census_list = []
        self.sorted = []
        with open(self.filename, 'r') as fileObject:
            fileData = fileObject.readlines()
            for line in fileData:
                match = re.search(r'(\d+)', line[213:300])  # Find the initial sequence of numbers
                if match:
                    numbers = match.group(1)
                    rest = line[226:300]  # Extract the remaining part
                else:
                    numbers = ""  # No numbers found
                    rest = line[213:300]   
                self.census_list.append(numbers.ljust(20) + rest)
            self.sorted = sort_by_letters(self.census_list)

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
