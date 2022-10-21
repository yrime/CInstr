import re

class StructPattern:
    def get_if_pattern(self, text):
        indexes = list()
        for match in re.finditer("[ \t\r\n;]+if[ \t\n\r]*\(", text):
            indexes.append(match.end())
        return indexes

    def get_else_pattern(self, text):
        indexes = list()
        for match in re.finditer("[\} \t\r\n]+else[\{ \r\t\n]*", text):
            indexes.append(match.end())
        return indexes

    def get_for_pattern(self, text):
        indexes = list()
        for match in re.finditer("[ \t\r\n;]+for[ \t\n\r]*\(", text):
            indexes.append(match.end())
        return indexes

    def get_while_pattern(self, text):
        indexes = list()
        for match in re.finditer("[ \t\n\r;]+while[ \t\n\r]*\(", text):
            indexes.append(match.end())
        return indexes

    def get_do_pattern(self, text):
        indexes = list()
        for match in re.finditer("[ \t\n\r;]+do[ \t\n\r]*\{", text):
            indexes.append(match.end())
        return indexes

    def get_switch_pattern(self, text):
        indexes = list()
        for match in re.finditer("[ \t\n\r;]+switch[ \r\t\n]*\(", text):
            indexes.append(match.end())
        return indexes

    def get_case_pattern(self, text):
        indexes = list()
        for match in re.finditer("[ \t\n\r;]+case[ \r\t\n]* [^:]+[ \n\t\r]*:", text):
            indexes.append(match.end())
        return indexes

    def get_return_start_pattern(self, text):
        indexes = list()
        for match in re.finditer("[ \t\n\r;]+return ", text):
            indexes.append(match.start())
        return indexes

    def get_break_start_pattern(self, text):
        indexes = list()
        for match in re.finditer("[ \r\t\n;]+break[ ]*;", text):
            indexes.append(match.start())
        return indexes

    def get_continue_start_pattern(self, text):
        indexes = list()
        for match in re.finditer("[ \t\r\n;]+continue[ ]*;", text):
            indexes.append(match.start())
        return indexes