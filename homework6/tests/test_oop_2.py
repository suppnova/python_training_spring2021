from collections import defaultdict

import pytest

from homework6.src.oop_2 import DeadlineError, HomeworkResult, Student, Teacher

mentor = Teacher("Baev", "Petr")
opp_teacher = Teacher("Samarin", "Aleksei")
lazy_student = Student("Roman", "Petrov")
good_student = Student("Lev", "Sokolov")

oop_hw = opp_teacher.create_homework("Learn OOP", 1)
docs_hw = opp_teacher.create_homework("Read docs", 5)
expired_homework = mentor.create_homework("Expired homework", 0)

result_1 = good_student.do_homework(oop_hw, "I have done oop_hw")
result_2 = good_student.do_homework(docs_hw, "I have done docs_hw too")
result_3 = lazy_student.do_homework(docs_hw, "done")


def test_homework_attributes():
    assert oop_hw.text == "Learn OOP" and str(docs_hw.deadline) == "5 days, 0:00:00"


def test_class_person_inheritance():
    assert mentor.first_name == "Petr" and opp_teacher.last_name == "Samarin"


def test_do_homework_returns_homework_result():
    assert isinstance(result_1, HomeworkResult)


def test_homework_result_accepts_only_homework_class():
    with pytest.raises(TypeError):
        HomeworkResult(good_student, "not a homework instance", "Solution")


def test_doing_expired_homework_raises_deadline_error():
    with pytest.raises(DeadlineError):
        lazy_student.do_homework(expired_homework, "Trying to do expired homework")


def test_check_homework_done_dict():
    opp_teacher.check_homework(result_1)
    opp_teacher_homeworks = opp_teacher.homework_done

    mentor.check_homework(result_1)
    teacher_homeworks = Teacher.homework_done

    assert opp_teacher_homeworks is teacher_homeworks


@pytest.mark.parametrize(
    ["homework_result", "expected_result"],
    [(result_1, True), (result_2, True), (result_3, False)],
)
def test_teacher_check_homework_result(
    homework_result: HomeworkResult, expected_result: bool
):
    assert opp_teacher.check_homework(homework_result) == expected_result


def test_teacher_homework_done_dict_unit():
    assert Teacher.homework_done[oop_hw] == ["I have done oop_hw"]


def test_reset_one_result():
    Teacher.reset_results(oop_hw)
    assert len(Teacher.homework_done[oop_hw]) == 0


def test_reset_all_results():
    Teacher.reset_results()
    assert Teacher.homework_done == defaultdict(list)
