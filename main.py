"""Точка входа проекта."""

from student import Student


def main():
    print("Практическое занятие №5")
    s = Student("Иван", "ИС-21")
    print(s, s.average([5, 4, 5]))


if __name__ == "__main__":
    main()
