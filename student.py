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
