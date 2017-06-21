import csv
def ignore_spaces_from_list(list_data,char):
    """ Take list and char and remove that char from the list"""
    while char in list_data:
        list_data.remove(char)
    return list_data
def ignore_char_from_string(my_string,char_in):
    """ Remove Specific Char from the list"""
    my_string=my_string.replace(char_in,'')
    return my_string
header_row=["Patient Name","Gender","DOB","Language","Acct#","Race","Ethnicity","Phone#","Email","Home Address","Reminder Method"]
class Patient(object):
    def __init__(self,list_data):
        """Takes a list and initilize patient object according to the list"""
        self.name=ignore_char_from_string(list_data[0],',')
        self.gender=list_data[1]
        self.dob=list_data[2]
        self.languague=list_data[3]
        self.acct_no=list_data[4]
        self.race=list_data[5]
        self.ethnicity=list_data[6]
        self.phone_no=list_data[7]
        self.email=list_data[8]
        self.home_address=list_data[9]
        self.reminder=list_data[10]
    def __repr__(self):
        """ Creates representation of the patient object"""
        return "%s, %s, %s, %s, %s,%s,%s, %s, %s, %s,%s " %(self.name,self.gender,self.dob,self.languague,
        self.acct_no,self.race,self.ethnicity,self.phone_no,self.email,self.home_address,self.reminder)
    def __eq__(self,other_patient):
        """ Takes Two patients and check whether they are same or not"""
        if(self.name==other_patient.name and self.gender==other_patient.gender and self.dob==other_patient.dob
        and self.languague==other_patient.languague and self.acct_no==other_patient.acct_no and self.race==other_patient.race
        and self.ethnicity==other_patient.ethnicity
        and self.phone_no==other_patient.phone_no and self.email==other_patient.email and self.home_address==other_patient.home_address
        and self.reminder==other_patient.reminder):
            return 1
        else:
            return 0
    def is_header_row(self):
        """ Return True if Current Patient is the header of the Patient object"""
        header_object=Patient(header_row)
        print header_object
        print self
        if(self==header_object):
            return True
            print True
        else:
            return False
#list to store all patients
patient_list=[]
# to keep track of Patient Header row
header_present=False
# open Csv file in readonly mode and parse it
with open('qc_training_csv_file.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        #print row
        # ignore spaces from the list
        row=ignore_spaces_from_list(row,'')
        if(len(row)==1):
            previous_patient=len(patient_list)-1
            if(previous_patient>0):
                patient_list[previous_patient].home_address+=" "+row[0]
        elif(len(row)>10):
            patient_in=Patient(row)
            if(patient_in.is_header_row()):
                if(header_present==False and len(patient_list)==0):
                    #print patient_in
                    patient_list.append(patient_in)
                    header_present=True
            else:
                #print patient_in
                patient_list.append(patient_in)
    f.close()
for item in patient_list:
    print item
with open('parsed_file.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for item in patient_list:
        #print item
        spamwriter.writerow(item.__repr__().split(','))
