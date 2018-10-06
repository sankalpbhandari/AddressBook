# Data related to Database Connection
DB_IP = "127.0.0.1"
DB_PORT = "3306"
DB_USERNAME = "root"
DB_PASSWD = "root"
DB_NAME = 'AddressBook'

# Mapping of Tables to their primary keys
MAPPING_IDS = {"CONTACT": "ContactID", "ADDRESS": "AddressID",
               "PHONE": "PhoneID", "DATE": "DateID"}
TABLES = ["CONTACT", "ADDRESS", "PHONE", "DATE"]

# The attributes of the table
MAPPING_TBL_VALUES = {
    "CONTACT_VALUES": '(Fname,Mname,Lname)',
    "ADDRESS_VALUES": '(ContactID,Address_type,Address,City,State,Zip)',
    "DATE_VALUES": '(ContactID,DateType,Date)',
    "PHONE_VALUES": '(PhoneType,ContactID,AreaCode,Number)'}

MAPPING_TBL_ATTR = {
    'CONTACT_ATTR': ['Fname', 'Mname', 'Lname'], 'ADDRESS_ATTR': [
        'ContactID', 'Address_type', 'Address', 'City', 'State', 'Zip'],
    'DATE_ATTR': ['ContactID', 'DateType', 'Date'], 'PHONE_ATTR': [
        'PhoneType', 'ContactID', 'AreaCode', 'Number']
}
