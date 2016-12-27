# from sys import argv

# # script, filename = argv

# # txt = open(filename) # this openes a file that written in the argv


filename = raw_input(">")
txt = open(filename)

print "Here's your file %r:" % filename # takes the file and prints it instead of %r
print txt.read() # prints the filename from the txt variable.




print "Type your filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()