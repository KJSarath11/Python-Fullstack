#get the list of country and city in a tuple
countries={
        "India":["Bangalore","Chennai","Delhi","Kolkata"],
        "USA":["Dallas","NY","Chicago"],
        "China":["Beijing","Shangai"]
    }

#o/p=[("India","Bangalore"),("India","Chennai").....]
# countries_=[]
# for country,cities in countries.items():
#     for city in cities:
#         countries_.append((country,city))

# print(countries_)

#comprehension
countries_=[(country,city) for country,cities in countries.items() for city in cities]
print(countries_)