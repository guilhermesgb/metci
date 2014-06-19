import random
import linecache

lookup = open('lookup.txt', 'a')

for num in range(445410):
    number = random.randint(1, 1781641)
    line = linecache.getline('dictionary.txt', number)
    lookup.write(line)

lookup.close()
    
