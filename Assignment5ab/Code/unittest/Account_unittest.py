#!/usr/bin/python
import csv
class Account(object):
    def __init__(self):
        """ Initilize Account object
        to default value
        """
        self.account_no=-1
        self.account_type=""
        self.balance=-1
    def set_account(self,a_id,a_type,a_balance):
        """ Sets values of all attributes of
        Account to Specified values
        """
        self.account_no=a_id
        self.account_type=a_type
        self.balance=a_balance

    def withdraw(self, amount):
        """ Withdraw Specified amount
        from current account
        """
        if self.balance > amount:
            self.balance-=amount
            self.makeupdate()
        return self.balance
    # MakeUpdate in Storage
    def makeupdate(self):
        """ Update Balance
         in the Storage
        """
        new_rows_list = []
        with open('customercom.csv', 'rb') as f:
            reader = csv.reader(f,delimiter=',')
            for row in reader:
                if(int(row[2])==self.account_no ):
                    row[4]=self.balance
                new_rows_list.append(row)
            f.close()
        with open('customercom.csv', 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(new_rows_list)
            f.close()
    # Deposit amount in account
    def deposit(self, amount):
        """ Deposit Specified amount
        to the Current Balance value
        """
        self.balance += amount
        self.makeupdate();
        return self.balance
    # Check Available balance
    def Checkbalance(self):
        return self.balance
    # Deposit Utility Bills
    def PayBills(self,amount):
        self.Transfer_Money(4,amount)
    # Return Account Types
    def get_account_type(self):
        return self.account_type
    # Overload equal operator
    def __eq__(self,other_account):
        if(self.balance==other_account.balance):
            return 1
        else:
            return 0
    # Overload Less than Operator
    def __lt__(self,other_account):
        if(self.balance<other_account.balance):
            return 1
        else:
            return 0
    # Overload Greater than Operator
    def __gt__(self,other_account):
        if(self.balance>other_account.balance):
            return 1
        else:
            return 0
    # Compare Amount of Two Accounts
    def CompareAccounts(self,other_account):
        if(self==other_account):
            return 0
        elif(self>other_account):
            return 1
        elif(self<other_account):
            return 2
        else:
            return 3
    def Transfer_Money(self,account_no,amount):
        """ Transfer amount from the Current open account_no
        to Specified account
        """
        previous_balance=self.balance;
        with open('customercom.csv', 'rb') as f:
            reader = csv.reader(f,delimiter=',')
            for row in reader:
                if(int(row[2])==account_no):
                    temp_customer=Customer(row[1])
                    temp_customer.open_account(int(row[2]))
                    if(temp_customer.account.balance!=-1):
                        self.withdraw(amount)
                        if(self.balance!=previous_balance):
                            temp_customer.account.deposit(amount)
# Global method to get if for new account

class Customer(object):
    # Constructor Initillizes attributes
    def __init__(self,name):
        self.c_name=name
        self.c_id=-1
        self.account=Account()
    def Request_new_account(self,account_type):
        """ Customer open a new account
        """
        self.c_id=self.get_customer_id()
        self.account.set_account(self.c_id,account_type,0)
        custmr=[self.c_id,self.c_name,self.c_id,account_type,0]
        with open('customercom.csv', 'ab') as f:
            writer = csv.writer(f)
            writer.writerow(custmr)
            f.close()
    def open_account(self,account_no):
        """ Open an existing account
        """
        #print "Hello"
        with open('customercom.csv', 'rb') as f:
            reader = csv.reader(f,delimiter=',')
            for row in reader:
                #print row
                if(int(row[2])==account_no):
                    if(row[1]==self.c_name):
                        self.c_id=int(row[0])
                        self.account.set_account(int(row[2]),row[3],int(row[4]))
                        return 1
            return 0
            f.close()
    def get_customer_id(self):
        with open('customercom.csv', 'rb') as f:
            reader = csv.reader(f,delimiter=',')
            for row in reader:
                #print row
                customer_id=int(row[0])
                customer_id+=1
            return customer_id
            f.close()

import unittest
class CustomerTestCases(unittest.TestCase):
    def test__init__(self):
        self.my_customer = Customer("Rabia")
        self.my_customer.c_id=11
        self.my_customer.account=Account()
        self.my_customer.account.set_account(11,"S",100)
    def test_balance(self):
        """
        Tests if balance is set successfully or not
        """
        self.test__init__()
        self.assertEqual(self.my_customer.account.balance,100,msg=" Balance not Set")
    def test_deposit(self):
        """
        Tests if depost Work properly
        """
        self.test__init__()
        self.my_customer.account.deposit(500)
        self.assertEqual(self.my_customer.account.balance,600,msg=" Balance Not Updated after deposit")
    def test_withdraw(self):
        """
        Tests if withdraw Work properly
        """
        self.test__init__()
        self.my_customer.account.withdraw(50)
        self.assertEqual(self.my_customer.account.balance,50,msg=" Balance Not Updated after withdraw")
        self.my_customer.account.withdraw(500)
        self.assertEqual(self.my_customer.account.balance,50,msg=" Withdraw Even when Not enough amount Available")
    def test_checkbalance(self):
        self.test__init__()
        self.assertEqual(self.my_customer.account.Checkbalance(),100,msg=" Checkbalance not works Properly")
    def test_transfermoney(self):
        """
        Tests if customer able to Transfer amount  Successfully
        """
        self.test__init__()
        # open an exisiting account as destination
        # amount should Transfer to pass test
        dest_customer=Customer("Gulnaz")
        dest_customer.open_account(5)
        prev_balance=dest_customer.account.Checkbalance()
        self.my_customer.account.Transfer_Money(5,50)
        self.assertEqual(self.my_customer.account.Checkbalance(),50,msg=" Trasfer from source Account")
        dest_customer.open_account(5)
        new_balance=dest_customer.account.Checkbalance()
        self.assertEqual(prev_balance+50,new_balance,msg=" Amount not comes in destination Account")
        # open an account that not exist
        # amount should not transfer to pass test
        self.test__init__()
        self.my_customer.account.Transfer_Money(15,50)
        self.assertEqual(self.my_customer.account.Checkbalance(),100,msg=" Amount Transfer But dest not exist")
    def test_PayBills(self):
        """
        Tests if customer able to paybills Successfully
        """
        self.test__init__()
        self.my_customer.account.PayBills(50)
        self.assertEqual(self.my_customer.account.Checkbalance(),50,msg=" Bills not Pay")
    def test_requestnewaccount(self):
        """
        Tests when request for new account is made it is
        opened or not
        """
        dest_customer=Customer("Tempcust")
        dest_customer.Request_new_account("S")
        dest_customer.account.deposit(500)
        acnt_no=dest_customer.account.account_no
        dest_customer.open_account(acnt_no)
        self.assertEqual(dest_customer.account.Checkbalance(),500,msg=" New Account Not Opened")
    def test_openaccount(self):
        """
        Tests if an account Open Suceesfully when exist
        and not opened when not exist
        """
        f_customer=Customer("huma")
        f_customer.open_account(2)
        self.assertNotEqual(f_customer.account.Checkbalance(),-1,msg=" Account Not Opened But it exists")
        s_customer=Customer("huma")
        s_customer.open_account(15)
        self.assertEqual(s_customer.account.Checkbalance(),-1,msg=" Account Open when it not exist")





if __name__ == '__main__':
    unittest.main()
