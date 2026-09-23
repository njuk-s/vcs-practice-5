"""Класс, добавленный в проект."""


class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def __str__(self):
        return f"{self.name} ({self.group})"

    def average(self, marks):
        """Средний балл по списку оценок."""
        return round(sum(marks) / len(marks), 2) if marks else 0.0

    def is_excellent(self, marks):
        """Отличник, если средний балл не ниже 4.5."""
        return self.average(marks) >= 4.5
