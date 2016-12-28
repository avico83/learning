ten_things = "Apple Orange Crows Telephone Light Sugar"
print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print 'Adding:', next_one
    stuff.append(next_one)
    print "There ard %d items now." % len(stuff)


print "There we go: ", stuff
# print "Let's do some things with stuff."
print "\nprints the first index in the list which is:", stuff[1]
print "\nprints the last item in the list which is: ", stuff[-1]
stuff_without_last = stuff.pop(-1)
print "\npops out the last item in the list which is:", stuff.pop()
print "\nprints the list without the last item that was: ", stuff_without_last
print "\nprints the current list:",' '.join(stuff)
print "\nprints only the items in the list stuff from location index\n3 through 5 (not including):\n" \
      "which they are:", ' # '.join(stuff[3:5])

print "\nThat was fun, goodbye!"

