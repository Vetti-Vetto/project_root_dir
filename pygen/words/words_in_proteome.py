from io import open
def read_file (file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content
file_name = 'english-common-words.txt'
content = read_file(file_name)
print(content)