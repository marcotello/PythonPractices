# Code

locations = {'North America': {'USA': ['Mountain View', 'Atlanta']}, 
     'Asia': {'India': ['Bangalore'], 'China': ['Shanghai']},
     'Africa': {'Egypt': ['Cairo']}}

# TODO: Print a list of all cities in the USA in alphabetic order.
american_cities = locations['North America']['USA']
american_cities.sort() 
print(1)
for city in american_cities:
    print(city)

# TODO: Print all cities in Asia, in alphabetic order, next to the name of the country
asian_countries = locations['Asia']
asian_cities = list()
print(2)
for country in asian_countries:
     asian_cities.append("{} - {}".format(asian_countries[country][0], country))
asian_cities.sort()
for city in asian_cities:
     print(city)