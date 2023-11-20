#this is to read the english-common-words.txt file, will be deleted in the final version of the project
from io import open
def read_file (file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content
file_name = 'C:/Users/mount/Downloads/softdev project/project_root_dir/pygen/words/english-common-words.txt'
content = read_file(file_name)
print(content)
