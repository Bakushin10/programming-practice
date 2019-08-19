class SimpleGradeBook(object):
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = []
    
    def report_grades(self, name, score):
        self._grades[name].append(score)
    
    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)
    
book = SimpleGradeBook()
book.add_student("Isaac Newton")
book.report_grades("Isaac Newton", 90)
print(book.average_grade("Isaac Newton"))


class BySubjectGradebook(object):
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = {}
    
    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        #if there is no values, then create default
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count

book = BySubjectGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 75)
book.report_grade('Albert Einstein', 'Math', 65)
book.report_grade('Albert Einstein', 'Gym', 90)
book.report_grade('Albert Einstein', 'Gym', 95)
print(book.average_grade('Albert Einstein'))
print(book._grades)

import collections
Grade = collections.namedtuple('Grade',('score', 'weight'))
print(Grade)