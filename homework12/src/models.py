from collections import defaultdict
from datetime import datetime, timedelta

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Homework(Base):
    __tablename__ = "homeworks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
    deadline = Column(DateTime)

    created = Column(DateTime)
    author_id = Column(Integer, ForeignKey("teachers.id"))
    author = relationship("Teacher", back_populates="created_homeworks")

    results = relationship("HomeworkResult", back_populates="homework")

    def __init__(self, text: str, deadline: timedelta, author: "Teacher"):
        super(Homework, self).__init__(
            text=text,
            deadline=datetime.now() + deadline,
            created=datetime.now(),
            author=author,
        )

    def is_active(self) -> bool:
        return datetime.now() < self.deadline


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    first_name = Column(String)
    homework_results = relationship("HomeworkResult", back_populates="author")

    def __repr__(self):
        return f"<Student(last_name={self.last_name}, first_name={self.first_name}>"

    def do_homework(self, hw: Homework, solution: str):
        if not hw.is_active():
            raise DeadlineError("You are late")
        return HomeworkResult(self, hw, solution)


class HomeworkResult(Base):
    __tablename__ = "homework_results"
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("students.id"))
    author = relationship("Student", back_populates="homework_results")

    homework_id = Column(Integer, ForeignKey("homeworks.id"))
    homework = relationship("Homework", back_populates="results")
    solution = Column(String)
    created = Column(DateTime)

    def __init__(self, author: Student, homework: Homework, solution: str):
        self.created = datetime.now()
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        super(HomeworkResult, self).__init__(
            author=author, solution=solution, homework=homework
        )


class DeadlineError(Exception):
    """Exception raised for deadline (if the task is already overdue)"""

    pass


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    first_name = Column(String)
    created_homeworks = relationship("Homework", back_populates="author")
    homework_done: dict[Homework, list[HomeworkResult]] = defaultdict(list)

    def __repr__(self):
        return f"<Teacher(last_name={self.last_name}, first_name={self.first_name}>"

    def create_homework(self, hw_text: str, days_for_hw: int) -> Homework:
        return Homework(hw_text, timedelta(days=days_for_hw), self)

    @staticmethod
    def check_homework(hw_result: HomeworkResult) -> bool:
        if len(hw_result.solution) < 5:
            return False
        if hw_result.solution not in Teacher.homework_done[hw_result.homework]:
            Teacher.homework_done[hw_result.homework].append(hw_result.solution)
        return True

    @staticmethod
    def reset_results(homework=None):
        if homework is None:
            Teacher.homework_done = defaultdict(list)
        else:
            Teacher.homework_done[homework] = []
