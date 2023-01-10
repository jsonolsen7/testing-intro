# import sys
# sys.path.insert(1, './code')
# import pytest
# import sqlite3
# import requests
# import os

# @pytest.mark.parametrize("inputs, expected_output", [
#     ((2, 3), 5),
#     ((-2, 3), 1),
#     ((2, -3), -1),
#     ((0, 0), 0)
# ])

# def test_addition(inputs, expected_output):
#     print("\nAddition Iteration - Test Start")
#     assert add(inputs[0], inputs[1]) == expected_output

# def add(a, b):
#     return a + b

# @pytest.fixture
# def setup_database():
#     connection = sqlite3.connect(":memory:")
#     cursor = connection.cursor()
#     cursor.execute("CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)")
#     sample_data = [
#         ('2020-01-01', 'BUY', 'IBM', 1000, 45.0),
#         ('2020-01-01', 'SELL', 'TSLA', 350, 200.0),
#     ]
#     cursor.executemany("INSERT INTO stocks VALUES(?, ?, ?, ?, ?)", sample_data)
#     yield connection

# def test_connection(setup_database):
#     cursor = setup_database
#     assert len(list(cursor.execute("SELECT * FROM stocks"))) == 2

# def test_file_exists():
#     assert os.path.exists('./requirements.txt')

# def test_file_creation():
#     create_file('./new_file.txt')
#     assert os.path.exists('./new_file.txt')

# def create_file(path):
#     with open(path, 'w') as f:
#         f.write('contents of file')

# def test_file_content():
#     with open('./new_file.txt', 'r') as f:
#         contents = f.read()
#     assert contents == 'contents of file'

# class TestCalculator:

#     def test_addition(self):
#         print("\nTest Calc Created for Addition")
#         calc = Calculator()
#         assert calc.add(2, 3) == 5
#         assert calc.add(2, 4) == 6
#         assert calc.add(2, -1) == 1
#         print("Test Completed for Addition")

#     def test_subtraction(self):
#         print("\nTest Calc Created for Subtraction")
#         calc = Calculator()
#         assert calc.subtract(2, 3) == -1
#         assert calc.subtract(2, 4) == -2
#         assert calc.subtract(2, -1) == 3
#         print("Test Completed for Subtraction")

#     def test_multiply(self):
#         print("\nTest Calc Created for Multiplication")
#         calc = Calculator()
#         assert calc.multiply(2, 4) == 8
#         print("Test Completed for Multiplication")

#     def test_division(self):
#         print("\nTest Calc Created for Division")
#         calc = Calculator()
#         assert calc.divide(4, 2) == 2
#         with pytest.raises(ZeroDivisionError):
#             calc.divide(8, 0)
#         print("Test Completed for Division")


# class Calculator:

#     def add(self, a, b):
#         print("Assertion Iteration - Complete")
#         return a + b

#     def subtract(self, a, b):
#         print("Assertion Iteration - Complete")
#         return a - b

#     def multiply(self, a, b):
#         print("Assertion Iteration - Complete")
#         return a * b
    
#     def divide(self, a, b):
#         print("Assertion Iteration - Complete")
#         try:
#             c = a / b
#         except ZeroDivisionError:
#             c = print("Can't divide by 0")
#             raise ZeroDivisionError
        
#         return c