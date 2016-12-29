import mystuff

my_stuff = {'apple': "I AM APPLES!"}
print my_stuff['apple']


mystuff.apple()

print "You need to print the module first and then the function\n" \
      "As this example:\n", mystuff.tangerine

print "-" * 50

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"
        self.tangerine1 = "This is a new object"


    def apples(self):
        print "I AM CLASSY APPLES"

thing = MyStuff() # This is the class name
thing.apples()# this is the function inside the class
print thing.tangerine# This is how you call an object within a class
print thing.tangerine1


# dict style

# MyStuff['apples']

print "-" * 50
print "Module Style:"
mystuff.apple()
print mystuff.tangerine

print "-" * 50
print "Class Style:"
thing = MyStuff()
thing.apples()
print thing.tangerine
print "-" * 50




