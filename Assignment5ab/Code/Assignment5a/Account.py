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



#######################################
############ Command Line Interface#####
def open_account_interface():
    while True:
        print "Enter Account No"
        read_account=raw_input()
        print "Enter name"
        read_name=raw_input()
        customer_=Customer(read_name)
        customer_.open_account(int(read_account))
        if(customer_.account.balance!=-1):
            Check_Account_Details_interface(customer_)
            return customer_
            break
        else:
            print "Enter valid Account NO and Name"


def Check_Account_Details_interface(customer_):
    while True:
        print "1: Press 1 to Deposit Money"
        print "2: Press 2 to get your Account Number"
        print "3: Press 3 to Check Balance"
        print "4: Press 4 to Withdraw Amount"
        print "5: Press 5 to Transfer Amount"
        print "6: Press 6 to Pay Bills"
        print "7: Press 7 to get Account Type"
        print "8: Press 8 to exit"
        read_Trun=raw_input()
        if(read_Trun=="8"):
            break
        elif(read_Trun=="1"):
            print "Enter amount to deposit"
            read_amount=raw_input()
            customer_.account.deposit(int(read_amount))
        elif(read_Trun=="2"):
            print customer_.account.account_no
        elif(read_Trun=="3"):
            print customer_.account.Checkbalance()
        elif(read_Trun=="4"):
            print "Enter amount to withdraw"
            read_amount=raw_input()
            customer_.account.withdraw(int(read_amount))
        elif(read_Trun=="5"):
            print "Enter other account to which to Transfer amount"
            read_account=raw_input()
            print "Enter Amount to Transfer"
            read_amount=raw_input()
            customer_.account.Transfer_Money(int(read_account),int(read_amount))
        elif(read_Trun=="6"):
            print "Enter Amount to PayBills"
            read_amount=raw_input()
            customer_.account.PayBills(int(read_amount))
        elif(read_Trun=="7"):
            print customer_.account.get_account_type()
        else:
            print "Enter valid Number"


# Command Line based Interface
while True:
    print "1: Press 1 to open a new Account"
    print "2: Press 2 to open an existing Account"
    print "3: Press 3 To Compare balance of Two accounts"
    print "4: Press 4 To exit"
    input_read=raw_input()
    if (input_read=="4"):
        break
    if (input_read=="1"):
        print "Please Enter your Name"
        read_name=raw_input()
        customer_=Customer(read_name)
        print "Please Specify Account Type. S for Saving and C for checking "
        while True:
            read_Type=raw_input()
            if(read_Type=="S"):
                customer_.Request_new_account("S")
                break
            elif(read_Type=="C"):
                customer_.Request_new_account("C")
                break
            else:
                print "Please Enter Valid Account Type"
        Check_Account_Details_interface(customer_)


    if(input_read=="2"):
        customer_=open_account_interface()

    if(input_read=="3"):
        customer_1=open_account_interface()
        print customer_1.account.Checkbalance()
        customer_2=open_account_interface()
        print customer_2.account.Checkbalance()
        value=customer_1.account.CompareAccounts(customer_2.account)

        if(value==0):
            print "balance Equal in these accounts"
        elif(value==1):
            print "1st Account balance is Greater than 2nd"
        else:
            print "1st Account balance is less than 2nd"
