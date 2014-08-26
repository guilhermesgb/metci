import random
import linecache
import sys

run_number = int(sys.argv[1])

if ( run_number % 3 == 0 ):
    size = 1000
elif ( run_number % 3 == 1 ):
    size = 10000
else:
    size = 15000

run_path = sys.argv[2]

for name in (run_path+"/dict.txt", run_path+"/lookup.txt"):

    word_file = open(name, 'w')

    for num in range(size):
        number = random.randint(1, 1781641)
        line = linecache.getline('words_source.txt', number)
        word_file.write(line)

    word_file.close()
