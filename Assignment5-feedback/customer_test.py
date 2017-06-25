"""
This file Contains test cases for Account and Customer Classes
pylint score 9.83/10
"""
import unittest
from customer import Customer


class CustomerTestCases(unittest.TestCase):
    """
    This class tests the customer class operations
    via unit tests
    """
    def test__init__(self):
        """
        This initialize Customer attribute of Customer test cases
        :return: None
        """
        self.my_customer = Customer("Rabia")
        self.my_customer.account.c_id = 11
        self.my_customer.account.account_no = 11
        self.my_customer.account.account_type = "S"
        self.my_customer.account.balance = 100

    def test_balance(self):
        """
        Tests if balance is set successfully or not
        :return: Assertion of test fail or pass
        """
        self.test__init__()
        self.assertEqual(self.my_customer.account.balance, 100, msg=" Balance not Set")

    def test_deposit(self):
        """
        Tests if deposit Work properly
        :return: Assertion of test fail or pass
        """
        self.test__init__()
        self.my_customer.deposit(500)
        self.assertEqual(self.my_customer.account.balance, 600,
                         msg=" Balance Not Updated after deposit")

    def test_withdraw(self):
        """
        Tests if withdraw Work properly
        :return: Assertion of test fail or pass
        """
        self.test__init__()
        self.my_customer.withdraw(50)
        self.assertEqual(self.my_customer.account.balance, 50,
                         msg=" Balance Not Updated after withdraw")
        self.my_customer.withdraw(500)
        self.assertEqual(self.my_customer.account.balance, 50,
                         msg=" Withdraw Even when Not enough amount Available")

    def test_check_balance(self):
        """
        Tests if Customer is able to check his balance
        :return:Assertion of test fail or pass
        """
        self.test__init__()
        self.assertEqual(self.my_customer.check_balance(), 100,
                         msg="Check balance not works Properly")

    def test_transfer_money(self):
        """
        Tests if customer able to Transfer amount  Successfully
        :return: Assertion of test fail or pass
        """
        self.test__init__()
        # open an existing account as destination
        # amount should Transfer to pass test
        dest_customer = Customer("Gulnaz")
        dest_customer.open_account(5)
        prev_balance = dest_customer.check_balance()
        self.my_customer.transfer_money(5, 50)
        self.assertEqual(self.my_customer.check_balance(), 50,
                         msg="Transfer from source Account")
        dest_customer.open_account(5)
        new_balance = dest_customer.check_balance()
        self.assertEqual(prev_balance+50, new_balance,
                         msg=" Amount not comes in destination Account")
        # open an account that not exist
        # amount should not transfer to pass test
        self.test__init__()
        self.my_customer.transfer_money(200, 50)
        self.assertEqual(self.my_customer.check_balance(), 100,
                         msg=" Amount Transfer But dest not exist")

    def test_pay_bills(self):
        """
        Tests if customer able to pay bills Successfully
        :return: Assertion of test fail or pass
        """
        self.test__init__()
        self.my_customer.pay_bills(50)
        self.assertEqual(self.my_customer.check_balance(), 50, msg=" Bills not Pay")

    def test_request_new_account(self):
        """
        Tests when request for new account is made it is
        opened or not
        :return: Assertion of test fail or pass
        """
        dest_customer = Customer("Tempcust")
        dest_customer.request_new_account("S")
        dest_customer.deposit(500)
        acnt_no = dest_customer.get_account_number()
        dest_customer.open_account(acnt_no)
        self.assertEqual(dest_customer.check_balance(), 500, msg=" New Account Not Opened")

    def test_open_account(self):
        """
        Tests if an account Open Suceesfully when exist
        and not opened when not exist
        :return: Assertion of test fail or pass
        """
        f_customer = Customer("huma")
        f_customer.open_account(2)
        self.assertNotEqual(f_customer.check_balance(), -1,
                            msg=" Account Not Opened But it exists")
        s_customer = Customer("huma")
        s_customer.open_account(15)
        self.assertEqual(s_customer.check_balance(), -1,
                         msg=" Account Open when it not exist")
if __name__ == '__main__':
    unittest.main()
