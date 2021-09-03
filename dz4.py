class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__( name, surname)
        self.grades = {}
        self.courses_attached = []

    def __str__(self):
        grades = []
        for grade in self.grades.values():
            grades += grade
        average_grade = sum(grades)/len(grades)
        res = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекцию: {average_grade}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a Lecturer")
            return
        grades_self = []
        grades_other = []
        for grade in self.grades.values():
            grades_self += grade
        aver_grade_self = sum(grades_self) / len(grades_self)
        for grade in other.grades.values():
            grades_other += grade
        aver_grade_other = sum(grades_other) / len(grades_other)
        return aver_grade_self < aver_grade_other

class Rewiewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f"Имя: {self.name} \nФамилия: {self.surname}"
        return res
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lec(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        grades = []
        for grade in self.grades.values():
            grades += grade
        average_grade = sum(grades)/len(grades)
        res = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {average_grade}\nКурсы в процессе : {','.join(self.courses_in_progress)} \nЗавершенные курсы: {','.join(self.finished_courses)}"
        return res
    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a Student")
            return
        grades_self = []
        grades_other =[]
        for grade in self.grades.values():
            grades_self += grade
        aver_grade_self = sum(grades_self) / len(grades_self)
        for grade in other.grades.values():
            grades_other += grade
        aver_grade_other = sum(grades_other) / len(grades_other)
        return aver_grade_self < aver_grade_other


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student2 = Student('Elena', 'Petrova', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['c+']
best_student2.courses_in_progress += ['c+']
best_student2.courses_in_progress += ['Python']

cool_lector = Lecturer("vasya", "pup")
cool_lector2 = Lecturer("ivan", "ivanov")
cool_lector.courses_attached += ['Python']
cool_lector.courses_attached += ['c+']
cool_lector2.courses_attached += ['c+']
cool_lector2.courses_attached += ['Python']

best_student.rate_lec(cool_lector, 'Python', 10)
best_student.rate_lec(cool_lector2, 'c+', 10)
best_student2.rate_lec(cool_lector2, 'c+', 15)
best_student.rate_lec(cool_lector, 'Python', 9)
best_student.rate_lec(cool_lector2, 'Python', 30)
best_student.rate_lec(cool_lector2, 'Python', 5)
some_rewiewer = Rewiewer('Some', 'Buddy')
some_rewiewer.courses_attached += ['Python']
some_rewiewer.courses_attached += ['c+']
some_rewiewer2 = Rewiewer('Petr', 'Smirnov')
some_rewiewer2.courses_attached += ['c+']
best_student.finished_courses += ['java']


best_student.rate_lec(cool_lector, 'Python', 10)
best_student.rate_lec(cool_lector2, 'c+', 10)
best_student2.rate_lec(cool_lector2, 'c+', 15)
best_student.rate_lec(cool_lector, 'Python', 9)
best_student.rate_lec(cool_lector2, 'Python',20)

some_rewiewer.rate_hw(best_student, 'Python', 10)
some_rewiewer.rate_hw(best_student, 'Python', 15)
some_rewiewer.rate_hw(best_student, 'Python', 5)
some_rewiewer2.rate_hw(best_student2, 'c+', 20)
def calc_aver_grade (students, course):
    grades = []
    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                grades += student.grades[course]
    aver_grade = sum(grades) / len(grades)
    return aver_grade
print(calc_aver_grade ([best_student, best_student2], "Python"))
def calc_aver_grade2 (lectors, course):
    grades2 = []
    for lector in lectors:
        if isinstance(lector, Lecturer):
            if course in lector.grades:
                grades2 += lector.grades[course]
    aver_grade = sum(grades2) / len(grades2)
    return aver_grade

print(calc_aver_grade2 ([cool_lector, cool_lector2], "Python"))
# print(cool_lector.courses_attached)
# print(cool_lector.grades)
# print(cool_lector2.grades)
# print(cool_lector > cool_lector2 )
# print(some_rewiewer)
# print(cool_lector)
# print(best_student.grades)
# print(best_student2.grades)
# print(best_student < best_student2)