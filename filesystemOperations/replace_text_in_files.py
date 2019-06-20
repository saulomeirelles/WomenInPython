"""
- iterate over text files in this dir
- print the number of occurrences of a certain word (e.g. "hello")
"""

import os

def write_file(name, content):
    file = open(name, 'w')
    file.write(content)
    file.close()


def read_file(name):
    file = open(name, 'r')
    content = file.read()
    file.close()
    return content


# write some files
write_file('1.txt', 'hello world')
write_file('2.txt', 'hello hello hello world')
write_file('3.txt', 'coffee banana apple')

# search and replace
look_for = 'hello'
replace_with = 'bye'
current_directory = os.getcwd()
ls = os.listdir(current_directory)
for name in ls:
    if name.endswith('.txt'):
        content = read_file(name)
        new_content = content.replace(look_for, replace_with)
        write_file(name, new_content)
