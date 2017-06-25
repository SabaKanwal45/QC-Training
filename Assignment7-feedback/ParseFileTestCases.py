"""
This file contains test cases  for ParseFile Class
pylint Score 9.68/10
"""
import unittest
import csv
from Csvparsing import ParseFile, Patient


class ParseFileTestCases(unittest.TestCase):
    """
    This class tests the ParseFile class operations
    via unit tests
    """

    def test__init__(self):
        """
        Initialize ParseFileTestCases attribute
        """
        self.parse_file = ParseFile()
        self.assertEqual(self.parse_file.list_data, [], "Parse File Initialization Fails")
        self.assertEqual(self.parse_file.row, 0, "Parse File Initialization Fails")

    def test_filter_file(self):
        """
         Tests if the input CSV file filters correctly
        """
        self.test__init__()
        self.parse_file.filter_file()
        output = [Patient(["Patient Name", "Gender", "DOB", "Language", "Acct#", "Race",
                           "Ethnicity", "Phone#", "Email", "Home Address",
                           "Reminder Method"]),
                  Patient(["Patient 1 Test", "M", "7/19/2068", "English", "1", "Declined",
                           "Declined", "(111)123-1234", "sample@example.com",
                           "street address city and state", "cell"]),
                  Patient(["Patient 2 Test", "M", "2/8/1999", "English", "2", "Declined",
                           "Declined", "(111)123-1234", "sample@example.com",
                           "RTN MAIL FROM: street address city and state", "<none>"]),
                  Patient(["Patient Name", "Gender", "DOB", "Language", "Acct#", "Race",
                           "Ethnicity", "Phone#", "Email", "Home Address",
                           "Reminder Method"]),
                  Patient(["Patient 3 Test", "M", "7/19/2068", "English", "3", "Declined",
                           "Declined", "(111)123-1234", "sample@example.com",
                           "street address city and state", "home"]),
                  Patient(["Patient 4 Test", "M", "2/8/1999", "English", "4", "Declined",
                           "Declined", "(111)123-1234", "sample@example.com",
                           "RTN MAIL FROM: street address city and state", "work"])]
        self.assertEqual(self.parse_file.list_data, output, "Parse File file Fails")

    def test_get_file_length(self):
        """
        Test whether get_file_length method of ParseFile works or not
        """
        self.test__init__()
        self.assertEqual(self.parse_file.get_file_length(), 0, msg="Get file length method fails")
        self.parse_file.filter_file()
        self.assertEqual(self.parse_file.get_file_length(), 6,
                         msg="Get file length method fails")

    def test_write_parsed_file(self):
        """
        Tests whether filter results are correctly written in to output file
        """
        self.test__init__()
        self.parse_file.filter_file()
        self.parse_file.write_parsed_file()
        index = 0
        with open('parsed_file.csv', 'rb') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self.assertEqual(row, self.parse_file.list_data[index].__repr__().split(','))
                index += 1
        csv_file.close()


if __name__ == '__main__':
    unittest.main()
