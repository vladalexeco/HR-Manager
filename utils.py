from enum import Enum, auto
from employee_person import EmployeePerson

class Utils:

    @staticmethod
    def mark_persons_with_difference(
            persons: list[EmployeePerson],
            difference_list: list[EmployeePerson]
    ):
        for index, person in enumerate(persons):
            if person in difference_list:
                persons[index].marked = True

    @staticmethod
    def reduce_absolute_path_to_simple_name(path: str):
        return path.split("/")[-1]

    @staticmethod
    def is_not_empty(iterable):
        return not len(iterable) == 0

class AnalyzeStatus(Enum):
    ANALYZED_ONE_READY = auto()
    ANALYZED_TWO_READY = auto()
    ANALYZED_ONE_TWO_READY = auto()
    NOT_ANALYZED = auto()
    FILES_HAVE_NOT_DIFFERENCES = auto()

ANALYZE_STATUS = "analyze_status"
FIRST_FILENAME = "first_filename"
SECOND_FILENAME = "second_filename"

