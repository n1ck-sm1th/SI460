#test their solution

import fileclass

myCensus = fileclass.census("mdgeo2010.dp")

print ("Test Num:")
#print(myCensus.searchByNum(60463))
myCensus.searchByNum(60463)

print ("Test District:")
#print(myCensus.searchByDistrict("Worton CDP"))
myCensus.searchByDistrict("Worton CDP")
