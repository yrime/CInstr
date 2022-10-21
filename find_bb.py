import re

import strucr_pattern


class FindBB:
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
                    indexes.append(iter + 1)
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

