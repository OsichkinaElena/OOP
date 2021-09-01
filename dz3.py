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


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['c+']
some_rewiewer = Rewiewer('Some', 'Buddy')
best_student.finished_courses += ['java']

cool_lector = Lecturer("vasya", "pup")
cool_lector.courses_attached += ['Python']
cool_lector.courses_attached += ['c+']
best_student.rate_lec(cool_lector, 'Python', 10)
best_student.rate_lec(cool_lector, 'c+', 10)
best_student.rate_lec(cool_lector, 'c+', 9)
best_student.rate_lec(cool_lector, 'Python', 9)
some_rewiewer.courses_attached += ['Python']
some_rewiewer.courses_attached += ['c+']
some_rewiewer.rate_hw(best_student, 'Python', 20)
some_rewiewer.rate_hw(best_student, 'c+', 20)
# print(cool_lector.courses_attached)
# print(cool_lector.grades)
# print(some_rewiewer)
# print(cool_lector)
print(best_student)
