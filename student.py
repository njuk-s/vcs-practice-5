"""Класс, добавленный в проект."""


class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def __str__(self):
        return f"{self.name} ({self.group})"
