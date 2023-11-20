import re

from pyparsing import WordStart
def read_words(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        words = re.findall(r'\b\w{3,}\b', data)
        return [word.upper() for word in words]

print(read_words('C:/Users/mount/Downloads/softdev project/project_root_dir/pygen/words/english-common-words.txt'))
def count_words(file_name):
    words = read_words(file_name)
    return len(words)

print("word count:", count_words('C:/Users/mount/Downloads/softdev project/project_root_dir/pygen/words/english-common-words.txt'))

#PROTEINS

import os

def read_sequence(file_path):
    with open(file_path, 'r') as file:
        word_count_dict = {}
        current_sequence = ''
        for line in file:
            if line.startswith('>'):
                if current_sequence:
                    word_count_dict[current_sequence] = sequence
                word = line[4:10]
                sequence = ''
                current_sequence = word
            else:
                sequence += line.strip()
        if current_sequence:
            word_count_dict[current_sequence] = sequence
        return word_count_dict

current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'C:/Users/mount/Downloads/softdev project/project_root_dir/human-proteome.fasta')
read_sequence = read_sequence(file_path)


print("All the keys in the dictionary:")
for key in read_sequence.keys():
    print(key)

print(f"Sequence associated with the key 'O95139': {read_sequence['O95139']}")

#searching for words

import os

words = read_words('C:/Users/mount/Downloads/softdev project/project_root_dir/pygen/words/english-common-words.txt')
proteome = read_sequence('C:/Users/mount/Downloads/softdev project/project_root_dir/human-proteome.fasta')

def search_words_in_proteome(words, sequences):
    word_count = {}
    for word in words:
        word_count[word] = 0
        for sequence in sequences.values():
            if word in sequence:
                word_count[word] += 1
                break
    return word_count

word_count = search_words_in_proteome(words, proteome)
for word, count in word_count.items():
    print(f"{word} found in {count} sequences")
