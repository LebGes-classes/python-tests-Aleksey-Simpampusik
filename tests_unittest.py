from functions import (
    add, divide, multiply, subtract
)

import unittest


class TestAdd(unittest.TestCase):
    """Тесты для сложения."""

    def test_add_basic(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(100, 200), 300)
        self.assertEqual(add(-2, -5), -7)
        self.assertEqual(add(2, 0), 2)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1000000, 2000000), 3000000)

    def test_add_float(self):
        self.assertAlmostEqual(add(2.5, 3.6), 6.1, places=7)
        self.assertAlmostEqual(add(-5.5, 2.5), -3.0, places=7)

    def test_add_type_error(self):
        with self.assertRaises(TypeError):
            add("2", 3)
        with self.assertRaises(TypeError):
            add(2, "3")
        with self.assertRaises(TypeError):
            add("2", "3")
        with self.assertRaises(TypeError):
            add(None, 3)
        with self.assertRaises(TypeError):
            add([1, 2], 3)
        with self.assertRaises(TypeError):
            add(2, True)
        with self.assertRaises(TypeError):
            add(True, 3)


class TestSubtract(unittest.TestCase):
    """Тесты для вычитания."""

    def test_subtract_basic(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(5, 8), -3)
        self.assertEqual(subtract(6, 0), 6)
        self.assertEqual(subtract(-3, -3), 0)
        self.assertEqual(subtract(0, 10), -10)
        self.assertEqual(subtract(-5, 3), -8)

    def test_subtract_float(self):
        self.assertAlmostEqual(subtract(4.6, 1.4), 3.2, places=7)
        self.assertAlmostEqual(subtract(3.14, 1.14), 2.0, places=7)

    def test_subtract_type_error(self):
        with self.assertRaises(TypeError):
            subtract("5", 2)
        with self.assertRaises(TypeError):
            subtract(5, "2")
        with self.assertRaises(TypeError):
            subtract(5, None)


class TestMultiply(unittest.TestCase):
    """Тесты для умножения."""

    def test_multiply_basic(self):
        self.assertEqual(multiply(3, 0), 0)
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-3, -1), 3)
        self.assertEqual(multiply(-14, 2), -28)
        self.assertEqual(multiply(2, -3), -6)
        self.assertEqual(multiply(3, 1), 3)
        self.assertEqual(multiply(1, 0), 0)

    def test_multiply_float(self):
        self.assertEqual(multiply(-10, -2.5), 25.0)
        self.assertEqual(multiply(5.2, 2), 10.4)
        self.assertAlmostEqual(multiply(0.5, 0.5), 0.25, places=7)
        self.assertEqual(multiply(-2, 0.5), -1.0)

    def test_multiply_type_error(self):
        with self.assertRaises(TypeError):
            multiply("3", 2)
        with self.assertRaises(TypeError):
            multiply(4, "5")
        with self.assertRaises(TypeError):
            multiply(None, 5)


class TestDivide(unittest.TestCase):
    """Тесты для деления."""

    def test_divide_basic(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(10, -2), -5.0)
        self.assertEqual(divide(0, 5), 0.0)
        self.assertEqual(divide(-15, -3), 5.0)

    def test_divide_float(self):
        self.assertEqual(divide(4.5, 3), 1.5)
        self.assertEqual(divide(4.5, 2.5), 1.8)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertAlmostEqual(divide(1, 3), 0.3333333333333333, places=12)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_divide_type_error(self):
        with self.assertRaises(TypeError):
            divide("1", 3)
        with self.assertRaises(TypeError):
            divide(10, "1000")
        with self.assertRaises(TypeError):
            divide(None, 2)


if __name__ == '__main__':
    unittest.main()

