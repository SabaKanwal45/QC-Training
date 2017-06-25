"""
This file contains code of patient class and file class that has Patient Data inside it
pylint Score --9.22/10
"""
import csv


def ignore_spaces_from_list(list_data, char):
    """
    Remove Specified char from List
    :param list_data: input list
    :param char: input character
    :return: list that not has char as item inside it
    """
    while char in list_data:
        list_data.remove(char)
    return list_data


def ignore_char_from_string(my_string, char_in):
    """
    Remove Specified character from the input string
    :param my_string: input string
    :param char_in:  input char
    :return: Modified string that does not have input char inside it
    """
    my_string = my_string.replace(char_in, '')
    return my_string


header_row = ["Patient Name", "Gender", "DOB", "Language", "Acct#", "Race", "Ethnicity",
              "Phone#", "Email", "Home Address", "Reminder Method"]


class Patient(object):
    """
    Patient class that stores some patient attributes and helps the file
    class to correctly parse the CSV file
    """
    def __init__(self, list_data):
        """
        initialize patient object according to the list
        :param list_data: input list
        """
        self.name = ignore_char_from_string(list_data[0], ',')
        self.gender = list_data[1]
        self.dob = list_data[2]
        self.languague = list_data[3]
        self.acct_no = list_data[4]
        self.race = list_data[5]
        self.ethnicity = list_data[6]
        self.phone_no = list_data[7]
        self.email = list_data[8]
        self.home_address = list_data[9]
        self.reminder = list_data[10]

    def __repr__(self):
        """
        Takes Patient object and create string representation of it
        :return: String representation of string
        """
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s " \
               % (self.name, self.gender, self.dob, self.languague, self.acct_no,
                  self.race, self.ethnicity, self.phone_no, self.email, self.home_address,
                  self.reminder)

    def __eq__(self, other_patient):
        """
        Takes Two patient Objects and checks whether they are equal or not
        :param other_patient: second patient object
        :return: 1 for True or 0 for False
        """
        if(self.name == other_patient.name and self.gender == other_patient.gender
           and self.dob == other_patient.dob and self.languague == other_patient.languague
           and self.acct_no == other_patient.acct_no and self.race == other_patient.race
           and self.ethnicity == other_patient.ethnicity and self.phone_no == other_patient.phone_no
           and self.email == other_patient.email and self.home_address == other_patient.home_address
           and self.reminder == other_patient.reminder):
            return 1
        else:
            return 0

    def is_header_object(self):
        """
        Checks if the current patient is the header object or not
        :return: 1 for True or 0 for False
        """
        header_object = Patient(header_row)
        if self == header_object:
            return 1
        else:
            return 0


class ParseFile(object):
    """
    This class has one list as its attribute and patient object

    """

    def __init__(self):
        """
        initialize list of patients to empty list
        """
        self.list_data = []
        self.row = 0

    def filter_file(self):
        """
        Opens a CSV file and filters it and save
        parsed results in list_data attribute of ParseFile
        """
        with open('qc_training_csv_file.csv', 'rb') as csv_file:
            reader = csv.reader(csv_file)
            for row_data in reader:
                row_data = ignore_spaces_from_list(row_data, '')
                if len(row_data) == 1 and self.row > 0:
                    previous_patient = self.list_data[self.row-1]
                    if not previous_patient.is_header_object():
                        self.list_data[self.row-1].home_address += " " + row_data[0]
                elif len(row_data) > 10:
                    new_patient = Patient(row_data)
                    self.list_data.append(new_patient)
                    self.row += 1
            csv_file.close()

    def write_parsed_file(self):
        """
        Write filter results from list_data attribute in to CSV file
        """
        with open('parsed_file.csv', 'wb') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for patient in self.list_data:
                writer.writerow(patient.__repr__().split(','))
            csv_file.close()

    def get_file_length(self):
        """
        :return: length of list_data attribute of ParseFile
        """
        return self.list_data.__len__()


input_file = ParseFile()
input_file.filter_file()
input_file.write_parsed_file()
