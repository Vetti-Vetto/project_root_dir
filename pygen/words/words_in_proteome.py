import re
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

def read_sequences(filename):
    with open(filename, 'r') as file:
        sequences = {}
        current_sequence = ''
        for line in file:
            if line.startswith('>'):
                if current_sequence:
                    sequences[protein_id] = current_sequence
                current_sequence = ''
                protein_id = line.split('|')[1]
            else:
                current_sequence += line.strip()
        if current_sequence:
            sequences[protein_id] = current_sequence
    return sequences

def main():
    sequences = read_sequences('C:/Users/mount/Downloads/softdev project/project_root_dir/human-proteome.fasta')
    print('Number of sequences read:', len(sequences))
    print('Sequence associated with the protein O95139:', sequences['O95139'])

if __name__ == '__main__':
    main()