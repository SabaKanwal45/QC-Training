#!/usr/bin/python
"""
This file contains Customer Class and one global function get_customer_id
pylint Score--10
"""
import csv
from Account import Account


class Customer(object):
    """
     Used to Create instance of Customer object
     Customer has three attributes
     -Customer name
     -Customer id--uniquely identify Customer
     -Account Object that keeps track of Customer Account
     Customer has some methods that enable customer instance to access his account
    """

    def __init__(self, name):
        """
        Constructor method that initialize customer attributes
        :param name: Takes Name of Customer to initialize Customer object
        """
        self.c_name = name
        self.c_id = -1
        self.account = Account()

    def request_new_account(self, account_type):
        """
        Customer Request a new account and New account
        is opened and returned
        :param account_type: Takes input from customer for account type saving S and checking C
        :return: new Opened Account
        """
        self.c_id = get_customer_id()
        self.account.set_account(self.c_id, account_type, 0)
        new_customer = [self.c_id, self.c_name, self.c_id, account_type, 0]
        with open('customer.csv', 'ab') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(new_customer)
        csv_file.close()

    def open_account(self, account_no):
        """
        Open an already existing account
        :param account_no: Takes account number to open an account
        :return: True if account open else return false
        """
        with open('customer.csv', 'rb') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                if int(row[2]) == account_no:
                    if row[1] == self.c_name:
                        self.c_id = int(row[0])
                        self.account.set_account(int(row[2]), row[3], int(row[4]))
                        return True
            csv_file.close()
            return False

    def withdraw(self, amount):
        """
        Withdraw Specified amount from current Customer account
        :param amount: Take input amount to withdraw
        :return: Modified balance attribute
        """
        return self.account.withdraw(amount)

    def deposit(self, amount):
        """
        Deposit Specified amount to the Current Balance value
        :param amount: input amount to deposit
        :return: Modified amount
        """
        return self.account.deposit(amount)

    def check_balance(self):
        """
        Customer able to check his current opened account
        :return: account balance
        """
        return self.account.balance

    def pay_bills(self, amount):
        """
        Customer is able to pay his Utility bills
        :param amount: Takes amount to pay
        :return: None
        """
        self.transfer_money(4, amount)

    # Return Account Types
    def get_account_type(self):
        """
        Customer is able to check his account type
        :return: Customer account type
        """
        return self.account.account_type

    def get_account_number(self):
        """
        Customer is able to check his account type
        :return: Customer account type
        """
        return self.account.account_no

    def compare_accounts(self, other_customer):
        """
        Make Comparison of Two Customer accounts
        :param other_customer: Take second Customer as parameter
        :return: 0 for equality, 1 for greater than and 2 for less than
        """
        if self.account == other_customer.account:
            return 0
        elif self.account > other_customer.account:
            return 1
        else:
            return 2

    def transfer_money(self, account_no, amount):
        """Transfer amount from the Current open account_no
        to Specified account
        :param account_no: Take destination account Number
        :param amount: Take amount to transfer
        :return: None
        """
        previous_balance = self.account.balance
        with open('customer.csv', 'rb') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                if int(row[2]) == account_no:
                    new_customer = Customer(row[1])
                    new_customer.open_account(int(row[2]))
                    if new_customer.account.balance != -1:
                        self.account.withdraw(amount)
                        if self.account.balance != previous_balance:
                            new_customer.account.deposit(amount)


def get_customer_id():
    """
    Has Access to Customer Storage
    :return: Id for new Customer that Uniquely identify a Customer
    """
    customer_id = 0
    with open('customer.csv', 'rb') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            customer_id = int(row[0])
            customer_id += 1
        csv_file.close()
    return customer_id
