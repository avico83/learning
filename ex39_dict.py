# things = ['a', 'b', 'c', 'd']
# print "this prints the first index which is:\t", things[1]
#
# things[1] = 'z'
# print "this replaces the 'a' with character\t", things[1]
#
# print things
#
# stuff = {'name': 'Avi', 'age': 33, 'height': 2 * 90}
# print "Access an item in a dict using variable, so my first names is", stuff['name']
#
# print stuff["age"]
# print stuff['height'] , "CM"
#
# stuff['city'] = "san-francisco"
# print stuff['city']
# #for each in stuff:
#  #   print stuff.viewkeys()
#
# stuff[1] = "Wow"
# stuff[2] = "Neato"
#
# del stuff['city']
# del stuff[1]
# del stuff[2]
#
# print stuff
#

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New-York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'FL': 'Jacksonville',
    'MI': 'Detroit',
    'NY': 'New-York',
    'OR': 'Portland',
    'TX': 'Texas'
}
cities['FL'] = 'Miami' #this adds new key and value to dict named cities

print cities

print '-' * 50
print "NY state has:", cities['NY']
print "OR state has:", cities['OR']
print '-' * 50

print "Michigan's abbreviation is:", states['Michigan']
print "Florida's abbreviation is:", states['Florida']
print '-' * 50

print "You need to look at this from inside to outside\n","Michigan has:", cities[states['Michigan']]
print "Florida has:", cities[states['Florida']]
print '-' * 50
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)
print '-' * 50

for state, abbrev in states.items():
    print "%s is abbreviated %s and has city %s" % (state,
           abbrev, cities[abbrev])
print '-' * 50
state = states.get('Texas')
if not state:
    print "Sorry, no texas."

city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is: %s" % city
