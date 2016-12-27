# a = 0
a = int(raw_input("> "))

numbers = []

while a < 6:
    print "At the top i is %i" % a
    numbers.append(a)

    a = a + 1
    print "Numbers now: ",  numbers
    print "At the bottom i is %i" % a

print "The numbers: "

for num in numbers:
    print num