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

# look for occurrence
look_for = 'hello'
current_directory = os.getcwd()
ls = os.listdir(current_directory)
for name in ls:
    if name.endswith('.txt'):
        content = read_file(name)
        occurrences = content.count(look_for)
        print(f"{name:<15} {occurrences}")
