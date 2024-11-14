from typing import Optional


class EmployeePerson:

    def __init__(self, card_number: str, surname: str, name: str, middle_name: Optional[str],
                 salary: Optional[str], notation: Optional[str], marked: bool = False):
        self.card_number = card_number
        self.surname = surname
        self.name = name
        self.middle_name = middle_name
        self.salary = salary
        self.notation = notation
        self.marked = marked

    def __eq__(self, other):
        if not isinstance(other, EmployeePerson):
            return NotImplemented

        return (self.surname.upper() == other.surname.upper()
                and self.name.upper() == other.name.upper()
                and self.card_number == other.card_number)

    def __hash__(self):
        return hash((self.surname.upper(), self.name.upper(), self.card_number))

    def __repr__(self):
        return (f"EmployeePerson(card_number={self.card_number}, surname={self.surname}, name={self.name}, "
                f"middle_name={self.middle_name}, salary={self.salary}, notation={self.notation}, marked={self.marked})")

    def get_surname_and_name(self) -> str:
        return f"{self.surname} {self.name}"
