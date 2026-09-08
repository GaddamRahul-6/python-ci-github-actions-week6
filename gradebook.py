"""Small gradebook module for CI demonstration."""

from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Student:
    """Represent a student and their marks."""
    name: str
    marks: tuple[float, ...]

    @property
    def average(self) -> float:
        return calculate_average(self.marks)

    @property
    def grade(self) -> str:
        return assign_grade(self.average)


def validate_mark(mark: float | int | str) -> float:
    """Validate a mark in the inclusive range 0..100."""
    try:
        value = float(mark)
    except (TypeError, ValueError) as exc:
        raise ValueError("Mark must be numeric.") from exc
    if not 0 <= value <= 100:
        raise ValueError("Mark must be between 0 and 100.")
    return value


def calculate_average(marks: list[float | int | str] | tuple[float | int | str, ...]) -> float:
    """Return the average of a non-empty set of marks."""
    values = [validate_mark(mark) for mark in marks]
    if not values:
        raise ValueError("At least one mark is required.")
    return sum(values) / len(values)


def assign_grade(average: float | int | str) -> str:
    """Assign a grade based on a percentage average."""
    value = validate_mark(average)
    if value >= 90:
        return "A"
    if value >= 80:
        return "B"
    if value >= 70:
        return "C"
    if value >= 60:
        return "D"
    return "F"


def build_student(name: str, marks: list[float | int | str]) -> Student:
    """Create a validated Student record."""
    clean_name = name.strip()
    if not clean_name:
        raise ValueError("Student name cannot be empty.")
    values = tuple(validate_mark(mark) for mark in marks)
    if not values:
        raise ValueError("At least one mark is required.")
    return Student(clean_name, values)
