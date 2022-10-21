import re

import strucr_pattern


class Check_bb:
    def __init__(self):
        self._indexes_bb = list()

    def __add_index(self, start, end):
        self._indexes_bb.append((start, end))

    def __iter_bb_fin(self, text, index):
        i = 0
        fi = 0
        while (True):
            if text[index + i] == '{':
                fi = fi + 1
            elif text[index + i] == '}':
                fi = fi - 1
                if fi == 0:
                    return index + i
            i = i + 1

    def get_func_bb(self, text):
        indexes = []
        fi = 0
        iter = 0
        for c in text:
            if c == "{":
                if fi == 0:
                    indexes.append(iter)
                fi = fi + 1
            elif c == "}":
                fi = fi - 1
            iter = iter + 1
        print(indexes)
        for match in re.finditer("\)[ \t]*\n?[ \t]*\{", text):
            if match.end() - 1 in indexes:
                fin = self.__iter_bb_fin(text, match.start())
                self.__add_index(match.end() - 1, fin)
        self.__get_under_bb(text)

    def __get_sup_bb(self, text, indexes):
        print("indexes")
## получть начало базового блока типа (){... или () ...
    def __check_var_bb_start(self, text, index):
        i = 0
        for c in text[index:]:
            if c == '{':
                return index + i + 1
            elif c == ';':
                return index + i + 1
            elif ((c != ' ') and (c != ';') and (c != '{') and (c != '\n') and (c != '\t')):
                return index + 1
            i = i + 1
## получить указатель на конец скобочной структуры ( () ( ()))
    def __check_var_bb(self, text, index):
        li = 0
        i = 0
        for c in text[index:]:
            if c == '(':
                li = li + 1
            elif c == ')':
                li = li - 1
                if li == 0:
                    return index + i + 1
            i = i + 1

    def __check_second_stru(self, text, listmain, listplus):
        irr = self.__check_var_bb_start(text, listmain[0] + listplus[0])
        print("second", text[irr - 4:irr])

    def __check_main_stru(self, text, listmain, listplus):
        inn = self.__check_var_bb(text, listmain[0] + listplus[0])
        irr = self.__check_var_bb_start(text, inn)
        print("under", listplus[0], text[listmain[0] + listplus[0]], "inn:", inn, text[inn - 1], "irr:", irr, text[irr - 1], text[inn - 1 : irr])

    def __find_first_symbol(self, text, symbol, index):
        i = 0
        for c in text[index:]:
            if c == symbol:
                return index + i
            i = i + 1

    def __get_under_bb(self, text):
        x = strucr_pattern.StructPattern()
        for i in self._indexes_bb:
            print("i",i)
            subtext = text[i[0] + 1:i[1]] ## i[0]:i[1] - 1
            inder_indexes_if = x.get_if_pattern(subtext) # ссылка на начало блока
            inder_indexes_else = x.get_else_pattern(subtext) # ссылка на начало блока
            inder_indexes_do = x.get_do_pattern(subtext) # ссылка на начало блока
            inder_indexes_for = x.get_for_pattern(subtext) # ссылка на начало блока
            inder_indexes_case = x.get_case_pattern(subtext) # ссылка на :
            inder_indexes_return = x.get_return_start_pattern(subtext) #ссылка на первый сивол
            inder_indexes_switch = x.get_switch_pattern(subtext) # ссылка на начало блока
            inder_indexes_while = x.get_while_pattern(subtext) # ссылка на начало блока
            inder_indexes_break = x.get_break_start_pattern(subtext) #ссылка на первый сивол
            inder_indexes_continue = x.get_continue_start_pattern(subtext) #ссылка на первый сивол

           # print(i[0], inder_indexes_if)
            if len(inder_indexes_if)>0:
                print("if")
                self.__check_main_stru(text, i, inder_indexes_if)
            if len(inder_indexes_else)>0:
                print("else")
                self.__check_var_bb_start(text, i, inder_indexes_else)
            if len(inder_indexes_for)>0:
                print("for")
                self.__check_main_stru(text, i, inder_indexes_for)
            if len(inder_indexes_while)>0:
                print("while")
                self.__check_main_stru(text, i, inder_indexes_while)
            if len(inder_indexes_switch)>0:
                print("switch")
                self.__check_main_stru(text, i, inder_indexes_switch)
            if len(inder_indexes_do)>0:
                print("do")
                self.__check_second_stru(text, i, inder_indexes_do)
            if len(inder_indexes_case) > 0:
                print("case")
                for icase in inder_indexes_case:
                    print(text[self.__find_first_symbol(text, 'c', i[0] + icase)])
            if len(inder_indexes_return) > 0:
                print("return")
                for iret in inder_indexes_return:
                    print(text[self.__find_first_symbol(text, 'r', i[0] + iret)])
            if len(inder_indexes_break) > 0:
                print("break")
                for ibreak in inder_indexes_break:
                    print(text[self.__find_first_symbol(text, 'b', i[0] + ibreak)])
            if len(inder_indexes_continue) > 0:
                print("continue")
                for icont in inder_indexes_continue:
                    print(text[self.__find_first_symbol(text, 'c', i[0] + icont)])
'''
####
        indices = []
        text2 = 'this is a text'
        insert = 'vstavit'
        indices.insert(0, 0)
        substr = []
        for i in indices[:-1]:
            start = indices[i]
            end = indices[i+1]
            substr.append(text2[start:end])
            substr.append(insert)
        if indices[-1] < len(text):
            substr.append(text[end:])
        result = ''.join(substr)

'''
       #     print("b",subtext[0], subtext[len(subtext)-1], text[i[0]], text[i[1]], text[i[0]+inder_indexes_if[0]], inder_indexes_else)
