# tests.py

import unittest
from functions.get_files_info import get_files_info


class TestFilesInfo(unittest.TestCase):
    def test_current_directory_get_files_info(self):
        result = get_files_info("calculator", ".")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIsInstance(result[0], str)
        # Check that main.py is in the results
        main_file_found = any("main.py:" in item for item in result)
        self.assertTrue(main_file_found, f"main.py not found in results: {result}")

    def test_pkg_directory_get_files_info(self):
        result = get_files_info("calculator", "pkg")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIsInstance(result[0], str)
        # Check that calculator.py is in the results
        calc_file_found = any("calculator.py:" in item for item in result)
        self.assertTrue(calc_file_found, f"calculator.py not found in results: {result}")

    def test_previous_directory_get_files_info(self):
        result = get_files_info("calculator", "..")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIsInstance(result[0], str)
        # Check that main.py is in the results
        main_file_found = any("main.py:" in item for item in result)
        self.assertTrue(main_file_found, f"main.py not found in results: {result}")


if __name__ == "__main__":
    unittest.main()


