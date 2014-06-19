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
