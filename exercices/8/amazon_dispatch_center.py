class EmployeeDidntWorked(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class EmployeeWorkedNegatively(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class EmployeeWorkedTooMuch(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class PayIsNegative(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class PayIsTooBig(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def pay_employee(employee, hours_worked):
    if hours_worked < 0:
        raise EmployeeWorkedNegatively("Heure négative")
    elif hours_worked == 0:
        raise EmployeeDidntWorked("Pas travaillé")
    elif hours_worked > 744:
        raise EmployeeWorkedTooMuch("Trop travaillé")
    else:
        if employee.pay > 100:
            raise PayIsTooBig("Trop payé")
        elif employee.pay < 0:
            raise PayIsNegative("Paie négative")
        else:
            employee.receive_salary(hours_worked*employee.pay)