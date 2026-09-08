import unittest

from gradebook import (
    Student,
    assign_grade,
    build_student,
    calculate_average,
    validate_mark,
)


class GradebookTests(unittest.TestCase):
    def test_boundary_marks(self):
        self.assertEqual(validate_mark(0), 0.0)
        self.assertEqual(validate_mark(100), 100.0)

    def test_invalid_marks(self):
        for value in (-1, 101, "abc"):
            with self.assertRaises(ValueError):
                validate_mark(value)

    def test_average(self):
        self.assertAlmostEqual(
            calculate_average([80, 90, 70]),
            80.0,
        )

    def test_empty_average(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_grade_boundaries(self):
        self.assertEqual(assign_grade(90), "A")
        self.assertEqual(assign_grade(80), "B")
        self.assertEqual(assign_grade(70), "C")
        self.assertEqual(assign_grade(60), "D")
        self.assertEqual(assign_grade(59.9), "F")

    def test_student_creation_and_properties(self):
        student = build_student("  Rahul  ", [80, 90])
        self.assertIsInstance(student, Student)
        self.assertEqual(student.name, "Rahul")
        self.assertEqual(student.average, 85.0)
        self.assertEqual(student.grade, "B")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            build_student("   ", [80])


if __name__ == "__main__":
    unittest.main()
