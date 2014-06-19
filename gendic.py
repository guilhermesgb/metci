# Authors: Guilherme Santos e Laercio Vitorino
# Date: 06/17/2014

# The code below is aimed to generate the
# dictionary.txt file with lots of words to be
# used to test the data structures required
# for the experiment.

import glob
directories = glob.glob('dictionaries/*.dic')

dictionary = open('dictionary.txt', 'a')

for dic in directories:
    text = open(dic)
    for line in text:
        new_line = line.split('/')
        for word in new_line:
            dictionary.write(word)
    text.close()

dictionary.close()
