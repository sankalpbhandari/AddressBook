import mysql.connector

import AddressBook.config.constants as const


class DBHandler:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.contactID = None

    def create_connect(self):
        try:
            self.conn = mysql.connector.connect(host=const.DB_IP,
                                                user=const.DB_USERNAME,
                                                password=const.DB_PASSWD,
                                                database=const.DB_NAME)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)

    def close_connect(self):
        try:
            self.conn.close()
        except Exception as e:
            print(e)

    def insert(self, table_name, values):
        try:
            add_data = "INSERT INTO %s %s VALUES %s" % (table_name,
                                                        const.CONTACT_VALUES,
                                                        values)
            print("Inserting data", add_data)
            self.cursor.execute(add_data)
            row_id = self.cursor.lastrowid
            if table_name == 'CONTACT':
                self.contactID = row_id
            print(row_id)
            self.conn.commit()
        except Exception as e:
            print(e)

    def delete(self, table_name, id):
        try:
            db_primary_key = const.mapping[table_name]
            delete_data = "DELETE FROM %s where %s = %s" % (table_name,
                                                            db_primary_key, id)
            print("Deleting data", delete_data)
            self.cursor.execute(delete_data)
            self.conn.commit()
        except Exception as e:
            print(e)

    def search(self, table_name):
        try:
            search_data = "SELECT * from %s" % table_name
            print("Searching data", search_data)
            self.cursor.execute(search_data)
            for data in self.cursor:
                print(data)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    a = DBHandler()
    a.create_connect()
    a.insert("CONTACT", '("Sankalp", "Sanjay", "Bhandari")')
    a.search("CONTACT")
    a.delete("CONTACT", a.contactID)
    a.close_connect()
    exit(0)
