class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rating:
                lecturer.rating[course] += [rate]
            else:
                lecturer.rating[course] = [rate]
        else:
            return 'Ошибка'

    def average_grade(self):
        grades_list = []
        for grade in self.grades.values():
            grades_list += grade
        average_grade = str(sum(grades_list) / len(grades_list))
        return average_grade

    def __str__(self):
        return (f'Студент \nИмя: {self.name} \nФамилия: {self.surname}'
                f'\nСредняя оценка за домашние задания: {self.average_grade()}'
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершённые курсы: {", ".join(self.finished_courses)}\n')

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка! Это не студент!'
        else:
            if self.average_grade() > other.average_grade():
                return f'У студента {self.name} {self.surname} лучше успеваемость, чем у {other.name} {other.surname}\n'
            else:
                return f'У студента {other.name} {other.surname} лучше успеваемость, чем у {self.name} {self.surname}\n'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating = {}

    def average_rate(self):
        rates_list = []
        for rate in self.rating.values():
            rates_list += rate
        average_rate = str(sum(rates_list) / len(rates_list))
        return average_rate

    def __str__(self):
        return (f'Лектор \nИмя: {self.name} \nФамилия: {self.surname}'
                f'\nСредняя оценка за лекции: {self.average_rate()}\n')

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка, это не лектор!'
        else:
            if self.average_rate() > other.average_rate():
                return f'У лектора {self.name} {self.surname} больше балов, чем у {other.name} {other.surname}\n'
            else:
                return f'У лектора {other.name} {other.surname} больше балов, чем у {self.name} {self.surname}\n'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Проверяющий \nИмя: {self.name} \nФамилия: {self.surname}\n'


student_1 = Student('Бутенко', 'Глеб', 'male')
student_1.courses_in_progress += ['Python', 'Git']

student_2 = Student('Ким', 'Андрей', 'female')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Git']

reviewer_1 = Reviewer('Егор', 'Парфенов')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Борис', 'Копылов')
reviewer_2.courses_attached += ['Git']

lecturer_1 = Lecturer('Федор', 'Железков')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Илья', 'Малов')
lecturer_2.courses_attached += ['Git']

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Git', 8)

reviewer_1.rate_hw(student_2, 'Python', 5)

student_1.rate_lecturer(lecturer_1, 'Python', 6)
student_1.rate_lecturer(lecturer_2, 'Git', 6)

student_2.rate_lecturer(lecturer_1, 'Python', 5)

print(student_1)
print(student_2)
print(reviewer_1)
print(reviewer_2)
print(lecturer_1)
print(lecturer_2)

print(student_1 > student_2)
print(lecturer_1 > lecturer_2)


def avg_grades(students_list, course):
    all_grades = []
    for student in students_list:
        if student.grades.get(course) is not None:
            all_grades += student.grades.get(course)
    all_grades_avg = str(sum(all_grades) / len(all_grades))
    print(f'Средняя оценка студентов за домашние задания по курсу {course}: {all_grades_avg}')


def avg_rates(lecturer_list, course):
    all_rates_list = []
    for lecturer in lecturer_list:
        if lecturer.rating.get(course) is not None:
            all_rates_list += lecturer.rating.get(course)
    all_rates_avg = str(sum(all_rates_list) / len(all_rates_list))
    print(f'Средняя оценка лекторов по курсу {course}: {all_rates_avg}')


avg_grades([student_1, student_2], 'Python')
avg_grades([student_1, student_2], 'Git')

avg_rates([lecturer_1, lecturer_2], 'Python')
avg_rates([lecturer_1, lecturer_2], 'Git')