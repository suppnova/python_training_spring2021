from homework5.src.oop_1 import Homework, Student, Teacher

teacher = Teacher("Baev", "Petr")
student = Student("Odintsova", "Natalia")
expired_homework = teacher.create_homework("Learn functions", 0)
create_homework_too = teacher.create_homework
oop_homework = create_homework_too("create 2 simple classes", 3)


def test_teacher_attribute():
    assert teacher.last_name == "Baev"


def test_student_attribute():
    assert student.first_name == "Natalia"


def test_homework_class_deadline():
    assert str(expired_homework.deadline) == "0:00:00"


def test_homework_class_text():
    assert expired_homework.text == "Learn functions"


def test_create_function_from_homework_method():
    assert str(oop_homework.deadline) == "3 days, 0:00:00"


def test_do_expired_homework():
    assert student.do_homework(expired_homework) is None


def test_do_oop_homework():
    assert isinstance(student.do_homework(oop_homework), Homework)
