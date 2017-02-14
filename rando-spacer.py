from sys import argv
import random

strings = argv[1:len(argv)+1]
split_strings = []

for string in strings:
    split_string = list(string)
    for _ in range(random.randrange(0,5)):
        split_string.insert(random.randrange(0,len(split_string))," ")
    split_string = "".join(split_string)
    split_strings.append(split_string)

print "".join(split_strings)

