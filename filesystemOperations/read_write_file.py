"""
Write some content in a file, then read it.
"""

def write_file(name, content):
    file = open(name, 'w')
    file.write(content)
    file.close()


def read_file(name):
    file = open(name, 'r')
    content = file.read()
    file.close()
    return content


fname = 'doc.txt'
write_file(fname, 'hello world')
print(read_file(fname))
