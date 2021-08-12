class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    # Not specific to an instance
    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


if __name__ == "__main__":
    p1 = Person("John")
    p2 = Person("George")
    print(Person.get_number_of_people())
