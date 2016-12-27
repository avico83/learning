x = "There are %d types of people." % 10
binary = "binary" # string
do_not = "don't" # string
y = "Those who know %s and those who knows %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False 
joke_evaluation = "Isn't that joke so funny?! %r" # this is taking %r and placing the "hilarious" as the string in the print


print joke_evaluation % hilarious  # the % sign is taking the hilarious boolean and prints it.

w = "This is left side of..." # string
e = 'a string with a right side.' # string

print w + e
