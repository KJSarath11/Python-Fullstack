#buildings and meters convert meter to feets
buildings={'burj khalifa':828,'shangai tower':632,'lotte world tower':554.5}
#1m=3.28ft
building_feet={}

for building,height in buildings.items():
    building_feet[building]=height*3.28
print(building_feet)

#comprehension
building_feet={building:height*3.28 for building,height in buildings.items()}
print(building_feet)