"""
This file contains test cases  for Patient Class
pylint Score 9.70/10
"""
import unittest
from Csvparsing import Patient, header_row, ignore_spaces_from_list


class PatientTestCases(unittest.TestCase):
    """
    This class tests the customer class operations
    via unit tests
    """

    def test__init__(self):
        """
        Tests if patient object attributes is correctly initialized correctly or not
        """
        input_list = ["Patient 1, Test", "", "M", "7/19/2068", "English", "1", "Declined",
                      "Declined", "(111)123-1234", "", "sample@example.com", "",
                      "street address", "", "cell"]
        output_list = ignore_spaces_from_list(input_list, "")
        self.patient = Patient(output_list)
        self.assertEqual(self.patient.name, "Patient 1 Test", msg="Patient Name is not Set")
        self.assertEqual(self.patient.gender, "M", msg="Patient gender is not set")
        self.assertEqual(self.patient.dob, "7/19/2068", msg="Patient DOB is not Set")
        self.assertEqual(self.patient.languague, "English",
                         msg="Patient languague is not Set")
        self.assertEqual(self.patient.acct_no, "1", msg="Patient Acct# is not Set")
        self.assertEqual(self.patient.race, "Declined", msg="Patient Race is not Set")
        self.assertEqual(self.patient.ethnicity, "Declined",
                         msg="Patient ethnicity is not Set")
        self.assertEqual(self.patient.phone_no, "(111)123-1234",
                         msg="Patient Phone# is not Set")
        self.assertEqual(self.patient.email, "sample@example.com",
                         msg="Patient email is not Set")
        self.assertEqual(self.patient.home_address, "street address",
                         msg="Patient home address is not Set")
        self.assertEqual(self.patient.reminder, "cell",
                         msg="Patient Reminder Method is not Set")

    def test__eq__(self):
        """
        Tests magic method of equality for patient objects
        """
        self.test__init__()
        input_list = ["Patient 1, Test", "", "M", "7/19/2068", "English", "1", "Declined",
                      "Declined", "(111)123-1234", "", "sample@example.com", "",
                      "street address", "", "cell"]
        output_list = ignore_spaces_from_list(input_list, "")
        second_patient = Patient(output_list)
        self.assertEqual(True, self.patient == second_patient,
                         msg=" Patient Equal Magic Method fails")
        second_patient = Patient(header_row)
        self.assertEqual(False, self.patient == second_patient,
                         msg=" Patient Equal Magic Method fails")

    def test_is_header_object(self):
        """
        Tests if header row is identified as header row
        """
        self.test__init__()
        self.assertEqual(False, self.patient.is_header_object(),
                         msg="Patient is_header_row method fails")
        second_patient = Patient(header_row)
        self.assertEqual(True, second_patient.is_header_object(),
                         msg="Patient is_header_row method fails")

if __name__ == '__main__':
    unittest.main()
