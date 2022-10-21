
import sys
import re
filename = sys.argv[1]
with open(filename) as file:
    data = file.read()

basebloks = []
funclist = []
outputstr = ""
def check_function(text):
    global outputstr
    li = 0
    fi = 0
    bo = False
    baseline1 = -1
    baseline2 = -1
    linenum = -1
    lines = text.split('\n')
    for line in lines:
        linenum = linenum + 1
        for c in line:
            if bo:
                if c == '{' and fi == 0:
                    funclist.append(linenum)
                    print('MACRO_FUNC')
                elif c == ';' and fi != 0:
                    print('MACRO_CALL')
                else:
                    bo = False
            if c == '(':
                li = li + 1
                print(line, 'li', li, linenum)
            elif c == ')':
                li = li - 1
                bo = True
                print(line, 'li', li, linenum)
            elif c == '{':
                fi = fi + 1
                if baseline1 == -1:
                    baseline1 = linenum
                else:
                    baseline2 = linenum - 1
                    basebloks.append((baseline1, baseline2))
                    baseline1 = -1
                print(line, 'fi', fi, linenum)
            elif c == '}':
                fi = fi - 1
                if baseline1 != -1:
                    baseline2 = linenum - 1
                    basebloks.append((baseline1, baseline2))
                    baseline1 = -1
                print(line, 'fi', fi, linenum)
        outputstr += (line + '\n')

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

print(basebloks, funclist)

print(outputstr)

with open(filename) as file:
    i = -1
    for line in file:
        i = i + 1
    #    print(line.rstrip(), i)
