"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        """
        Klassi konstruktor.

        :param firstname: Isiku eesnimi
        :param lastname: Isiku perekonnanimi
        :param age: Isiku vanus
        """
        self.firstname = ""
        self.lastname = ""
        self.age = 0

    pass


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname="", lastname="", age=0):
        """
        Klassi konstruktor.

        :param firstname: Isiku eesnimi
        :param lastname: Isiku perekonnanimi
        :param age: Isiku vanus
        """
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    pass


if __name__ == '__main__':
    # empty usage

    # 3 x person usage
    person = Person()
    person.firstname = "Faking"
    person.lastname = "Ret"
    person.age = 69
    print(person.firstname, person.lastname, person.age)

    # 3 x student usage
    student = Student("a", "b", 1)
    print(student.firstname, student.lastname, student.age)
    pass
