# Authors: Guilherme Santos e Laercio Vitorino
# Date: 06/18/2014

# The code below is aimed to generate the
# lookup.txt file with lots of words to be
# used to test the data structures required
# for the experiment.

import random
import linecache

lookup = open('lookup.txt', 'a')

for num in range(445410):
    number = random.randint(1, 1781641)
    line = linecache.getline('dictionary.txt', number)
    lookup.write(line)

lookup.close()
    
