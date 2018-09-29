# Data related to Database Connection
DB_IP = "127.0.0.1"
DB_PORT = "3306"
DB_USERNAME = "root"
DB_PASSWD = "password"
DB_NAME = 'AddressBook'

# Mapping of Tables to their primary keys
mapping = {"CONTACT": "ContactID", "ADDRESS": "AddressID", "PHONE": "PhoneID",
           "DATE": "DateID"}

# The attributes of the table
CONTACT_VALUES = '(Fname,Lname,Lname)'
ADDRESS_VALUES = '(AddressID,ContactID,Address_type,Address,City,State,Zip)'
DATE_VALUES = '(DateID,ContactID,DateType,Date)'
PHONE_VALUES = '(PhoneID,PhoneType,ContactID,AreaCode,Number)'
