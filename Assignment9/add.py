"""add number of the form
add(5)(10)(15)any arbitrary number of
paranthesis and result the sum of numbers"""

statement=raw_input(); #take statement as input
if(statement[0:3]=="add"):
    statement=statement[3:]
    no_list=[]
    c_no=""
    i=0
    balance_pren=True
    Error=False
    while i!=len(statement):
        print statement
        if(statement[i]=="("):
            c_no=""
            c_int=0
            i=i+1
            balance_pren=not(balance_pren)
            while(statement[i].isdigit()):
                c_no+=statement[i];
                i=i+1
            if(statement[i]==")"):
                if(len(c_no)>0):
                    c_int=int(c_no)
                    no_list.append(c_int)
                    print "number %s" %c_int
                    balance_pren=not(balance_pren)
            else:
                Error=True
        else:
            Error=True
        i=i+1
    if(not Error):
        total=0
        for item in no_list:
            total+=item
        print "Sum is %s"% total
    else:
        print "Error Message: Parenthesis Error   "
