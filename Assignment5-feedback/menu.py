"""
This File Contains Menu for Customer Account Operations
pylint Score--9.08
"""
# pylint: disable-msg=C0103
from customer import Customer


def open_account_interface():
    """
    Prompt User to Enter valid account no and Customer Name
    :return: Customer instance for Current User
    """
    while True:
        print "Enter Account No"
        read_account = raw_input()
        print "Enter name"
        read_username = raw_input()
        current_customer = Customer(read_username)
        current_customer.open_account(int(read_account))
        if current_customer.check_balance() != -1:
            check_account_details_interface(current_customer)
            return current_customer
        else:
            print "Enter valid Account NO and Name"


def check_account_details_interface(input_customer):
    """
    Shows Menu to Customer-- Customer is able to get his account details
    :param input_customer: Takes Customer instance as parameter
    :return: None
    """
    while True:
        print "1: Press 1 to Deposit Money"
        print "2: Press 2 to get your Account Number"
        print "3: Press 3 to Check Balance"
        print "4: Press 4 to Withdraw Amount"
        print "5: Press 5 to Transfer Amount"
        print "6: Press 6 to Pay Bills"
        print "7: Press 7 to get Account Type"
        print "8: Press 8 to exit"
        read_menu = raw_input()
        if read_menu == "8":
            break
        elif read_menu == "1":
            print "Enter amount to deposit"
            read_amount = raw_input()
            input_customer.deposit(int(read_amount))
        elif read_menu == "2":
            print input_customer.get_account_number()
        elif read_menu == "3":
            print input_customer.check_balance()
        elif read_menu == "4":
            print "Enter amount to withdraw"
            read_amount = raw_input()
            input_customer.withdraw(int(read_amount))
        elif read_menu == "5":
            print "Enter other account to which to Transfer amount"
            read_account = raw_input()
            print "Enter Amount to Transfer"
            read_amount = raw_input()
            input_customer.transfer_money(int(read_account), int(read_amount))
        elif read_menu == "6":
            print "Enter Amount to PayBills"
            read_amount = raw_input()
            input_customer.pay_bills(int(read_amount))
        elif read_menu == "7":
            print input_customer.get_account_type()
        else:
            print "Enter valid Number"

# Command Line based Interface
while True:
    print "1: Press 1 to open a new Account"
    print "2: Press 2 to open an existing Account"
    print "3: Press 3 To Compare balance of Two accounts"
    print "4: Press 4 To exit"
    input_read = raw_input()
    if input_read == "4":
        break
    if input_read == "1":
        print "Please Enter your Name"
        read_name = raw_input()
        customer = Customer(read_name)
        print "Please Specify Account Type. S for Saving and C for checking "
        while True:
            read_Type = raw_input()
            if read_Type == "S":
                customer.request_new_account("S")
                break
            elif read_Type == "C":
                customer.request_new_account("C")
                break
            else:
                print "Please Enter Valid Account Type"
        check_account_details_interface(customer)
    if input_read == "2":
        customer = open_account_interface()
    if input_read == "3":
        customer1 = open_account_interface()
        print customer1.check_balance()
        customer2 = open_account_interface()
        print customer2.check_balance()
        value = customer1.compare_accounts(customer2)
        if value == 0:
            print "balance Equal in these accounts"
        elif value == 1:
            print "1st Account balance is Greater than 2nd"
        else:
            print "1st Account balance is less than 2nd"
