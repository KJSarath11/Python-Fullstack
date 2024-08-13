#wapt city and population into dictionary
cities={'Tokyo','Delhi','Shangai','Mumbai'}
populations={'38','25','23','21'}
city_population={}

for city,population in zip(cities,populations):
    city_population[city]=population
print(city_population)

city_population={city:population for city,population in zip(cities,populations)}
print(city_population)