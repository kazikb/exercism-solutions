# defaultdict tworzy obiekt dictionary z domyślnym typem danych.
# https://docs.python.org/3/library/collections.html#collections.defaultdict

from collections import defaultdict

class School:
    def __init__(self):
        self._student_list = defaultdict(list)
        self._student_added_log = []

    def add_student(self, name, grade):
        student_exist = False
        for grade_list in self._student_list.values():
            if name in grade_list:
                self._student_added_log.append(False)
                student_exist = True
                break
        if not student_exist:
            self._student_list[grade].append(name)
            self._student_added_log.append(True)

    def roster(self):
        return_roster = []
        self._student_list = dict(sorted(self._student_list.items()))
        for key in self._student_list.keys():
            return_roster.extend(sorted(self._student_list[key]))
        return return_roster

    def grade(self, grade_number):
        return sorted(self._student_list.get(grade_number, []))

    def added(self):
        return self._student_added_log
