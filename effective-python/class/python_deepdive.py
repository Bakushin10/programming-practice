# class Student(object):
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         print(self)

class Student(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @classmethod
    def from_string(cls, name_str):
        first_name, last_name = map(str, name_str.split(' '))
        print(cls)
        student = cls(first_name, last_name)
        return student

class School(Student):
    pass


scott = School.from_string('Scott Robinson')