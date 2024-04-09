import pickle
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    if groups:
        return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
        return list(set(group.specialty.name for group in groups))


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        try:
            while True:
                student = pickle.load(pickle_file)
                students.append(student)
        except EOFError:
            pass
    return students
