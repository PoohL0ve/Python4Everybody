# read each line
# split each word into a list
# if the word is not in the list add it
# when the list is completed, sort it

list_of_words = []
find_file = input('Enter file name: ')
search_file = open(find_file)

for line in search_file :
    no_space = line.strip()
    separated_word = no_space.split(' ')
    for word in separated_word :
        if not word in list_of_words :
            list_of_words.append(word)
fixed_list = sorted(list_of_words)            
print(fixed_list)    