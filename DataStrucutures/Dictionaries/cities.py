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
asean_cities = ['Asia']