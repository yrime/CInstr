
import sys
import re
filename = sys.argv[1]
with open(filename) as file:
    data = file.read()

def check_function(text):
    li = 0
    fi = 0
    lines = text.split('\n')
    for line in lines:
        print(line)

def nullstr_remover(text):
    lines = text.split('\n')
    new_lines = []
    for line in lines:
        if len(line) > 0 and not line.isspace():
            new_lines.append(line)
    return '\n'.join(new_lines)

def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)#def check_line(line):

ou = comment_remover(data)
oun = nullstr_remover(ou)
check_function(oun)
filename = sys.argv[1]
with open(filename) as file:
    i = -1
    for line in file:
        i = i + 1
        print(line.rstrip(), i)
