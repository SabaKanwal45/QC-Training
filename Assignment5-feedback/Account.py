#!/usr/bin/python
"""
This File contains Account Class
pylint Score--10.0
"""
import csv


class Account(object):
    """
    Account class has three attributes
    1)account_no-- Each Customer has its own unique account
    2)account_type-- has two possible values S for saving and C for checking
    3)balance--Stores Current balance of customer
    Account Class has some methods to enable bank account operations  for Customer
    """

    def __init__(self):
        """
        Initilaize Account object
        to default value
        """
        default_value = -1
        self.account_no = default_value
        self.account_type = ""
        self.balance = default_value

    def set_account(self, a_id, a_type, a_balance):
        """
        Set Account attribute values
        :param a_id: get input of account_id
        :param a_type: get input of account type
        :param a_balance: get input of new balance
        :return: Modified Object
        """
        self.account_no = a_id
        self.account_type = a_type
        self.balance = a_balance
        return self

    def withdraw(self, amount):
        """
        Withdraw Specified amount from current account
        :param amount: Take input amount to withdraw
        :return: Modified balance attribute
        """
        if self.balance > amount:
            self.balance -= amount
            self.make_update()
        return self.balance

    def make_update(self):
        """
        Update Balance in the Storage
        :return:None
        """
        new_rows_list = []
        with open('customer.csv', 'rb') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                if int(row[2]) == self.account_no:
                    row[4] = self.balance
                new_rows_list.append(row)
            csv_file.close()
        with open('customer.csv', 'wb') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(new_rows_list)
            csv_file.close()

    def deposit(self, amount):
        """
        Deposit Specified amount to the Current Balance value
        :param amount: input amount to deposit
        :return: Modified amount
        """
        self.balance += amount
        self.make_update()
        return self.balance

    def __eq__(self, other_account):
        """
        Magic Equality method for Account instance
        :param other_account: Take second account as parameter
        :return: True for equal and False for unequal
        """
        if self.balance == other_account.balance:
            return 1
        else:
            return 0

    def __lt__(self, other_account):
        """
        Magic less than method for Account instances
        :param other_account: Take second account as parameter
        :return: True for less than else return false
        """
        if self.balance < other_account.balance:
            return 1
        else:
            return 0

    def __gt__(self, other_account):
        """
        Magic greater than method for Account instances
        :param other_account: Take second account as parameter
        :return: true if condition satisfied else return false
        """
        if self.balance > other_account.balance:
            return 1
        else:
            return 0
