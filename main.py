
import sys
import re

import check_c_bb

filename = sys.argv[1]
with open(filename) as file:
    data = file.read()

basebloks = []
funclist = []
outputstr = ""

inputstr = "this->input.str"

def check_fi(text, index):
    i = 0
    fi = 0
    while(True):
        if text[index + i] == '{':
            fi = fi + 1
        elif text[index + i] == '}':
            fi = fi - 1
            if fi == 0:
                return index + i
        i = i + 1

def check_li(text, index):
    i = 0
    li = 0
    while(True):
        if text[index + i] == '(':
            li = li + 1
        elif text[index + i] == ')':
            li = li - 1
            if li == 0:
                return index + i
        i = i + 1

def func_bb(text):
    li = 0
    fi = 0
    fi_prev = 0;
    li_prev = 0
    arr = []
    outstr = ""
    outstr = re.sub("\)[ \t]*\n?[ \t]*\{", ")\n{\n"+inputstr, text)
    outstr = re.sub("}", "\n"+inputstr + "\n}", outstr)

    for match in re.finditer("\)[ \t]*\n?[ \t]*\{", text):
        print('g', match.start())
        arr.append(match.start())
        print(text[match.start()])
        print(text[check_fi(text, match.end() - 1)])
    for match in re.finditer("}", text):
        print('gg', match.start())
        print(text[match.start()])
        arr.append(match.start())
    for match in re.finditer("[ \t\n;]+if[ \t\n]*\(", text):
        print('ggg', match.start())
        arr.append(match.start())
        print(text[match.start()])
    for match in re.finditer("[ \t\n;]+for[ \t\n]*\(", text):
        print('f', match.start())
        arr.append(match.start())
        print(text[match.start()])
    for match in re.finditer("[ \t\n;]+while[ \t\n]*\(", text):
        print('ff', match.start())
        arr.append(match.start())
        print(text[match.start()])
    for match in re.finditer("[ \t\n;]+do[ \t\n]*\{", text):
        print('fff', match.start())
        arr.append(match.start())
        print(text[match.start()])
    for match in re.finditer("[ \t\n;]+switch[ \t\n]*\(", text):
        print('fff', match.start())
        arr.append(match.start())
        print(text[match.start()])
    for match in re.finditer("[ \t\n;]+case[ \t\n]* ", text):
        print('fff', match.start())
        arr.append(match.start())
        print(text[match.start()])
    for match in re.finditer("[ \t\n;]+return ", text):
        print('rrr', match.start())
        arr.append(match.start())
        print(text[match.start()])
    print(arr)
    #"[ \t\n;]+if[ \t]*\("
    #"[ \t\n;]+for[ \t]*\("
    #print(outstr)

   # print(re.sub("\([*.+]\)['\n' | ' ']\{", "\([*.]\)['\n' | ' ']\{[*.]\}"[:-1] + "\n"+inputstr+"}", outstr))
    lines = text.split('\n')
    for line in lines:
        for c in line:
            if c == '(':
                li_prev = li
                li = li + 1
            elif c == ')':
                li_prev = li
                li = li - 1
            elif c == '{':
                fi_prev = fi
                fi = fi + 1
                if li_prev != 0:
                    print("base block start")
            elif c == '}':
                fi_prev = fi
                fi = fi - 1
            else:
                fi_prev = 0
                li_prev = 0
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

func_bb(oun)


x = check_c_bb.Check_bb()
x.get_func_bb(oun)
