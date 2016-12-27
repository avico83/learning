# close - Closes the file --> f.close
# read - read the file --> f.read
# readline - read one line in the file --> f.readline
# truncate - empties the file !!!! 
# write ('stuff') - write stuff into the file


from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that hit CTRL-C (C^)."
print "If you do want that, hit RETURN."

raw_input("?")
print "Opening the file..."
target = open(filename, 'a') # a = append to file, w = write to file, r = read from file.

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1= raw_input("line 1: ")
line2= raw_input("line 2: ")
line3= raw_input("line 3: ")

print "I'm going to write these to the file..."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally w'ell close it."
target.close()
a  = open(filename)
print a.read()

