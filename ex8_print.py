# this takes the format string %r and place it in the parentesis for the word
# formatter.

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)


print formatter % ("one", "two", "three", "four")


# prints the words True/False
print formatter % (True, False, False, True)

print (formatter, formatter, formatter, formatter)

# dont forget the commas at the end of each line and the quotes of each sentence.

print formatter % ("I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight"
	)

