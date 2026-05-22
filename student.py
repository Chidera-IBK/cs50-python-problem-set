class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    students = get_student()
    print(students)

def get_student():
    name = input("What's your name? ")
    house = input("What's your House? ")

    return Student(name, house)

main()




