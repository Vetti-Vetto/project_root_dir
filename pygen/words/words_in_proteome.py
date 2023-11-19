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