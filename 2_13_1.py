class People():

    def __init__(self, name, surname, age, faculty, rank, subject):
        self.name = name
        self.surname = surname
        self.age = age
        self.faculty = faculty
        self.rank = rank
        self.subject = subject


class Student(People):

    def __init__(self, well, group, name, surname, age, faculty, rank, subject):
        super().__init__(name, surname, age, faculty, rank, subject)
        self.well = well
        self.group = group

    def inf_students(self):
        print(f"{self.name}, {self.surname}, {self.age}, {self.faculty}, {self.rank}, {self.subject},"
              f" {self.well}, {self.group}")


class Teacher(People):
    def __init__(self, salary, experience, groups, name, surname, age, faculty, rank, subject):
        super().__init__(name, surname, age, faculty, rank, subject)
        self.experience = experience
        self.salary = salary
        self.groups = groups

    def inf_teacher(self):
        print(f"{self.name}, {self.surname}, {self.age}, {self.faculty}, {self.rank}, {self.subject},"
              f" {self.salary}, {self.experience}, {self.groups}")


student = Student(name="Boris", surname="Steg", age=3, faculty="ElIT", rank="master",
                  subject=["Python", "SQL", "Algorithms"], well=3, group="PM")
teacher = Teacher(name="Tatyana", surname="Suhco", age=3, faculty="ElIT", rank="Ph.D",
                  subject=["Python", "Algorithms"], experience=20, salary=500, groups=["PM", "TP", "ITP"])
student.inf_students()
teacher.inf_teacher()
