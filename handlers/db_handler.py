import mysql.connector
import AddressBook.config.constants as const
from AddressBook.data.data_manipulation import DataManipulation


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

    def create(self, table_name, values):
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

    def update(self, table_name, id, data):
        try:
            update_data = "UPDATE %s set %s where %s=%s" % (table_name, data, const.MAPPING_IDS.get(table_name), id)
            print("Updating data", update_data)
            self.cursor.execute(update_data)
            self.conn.commit()
        except Exception as e:
            print(e)
            print("No Updated")

    def delete(self, table_name, id):
        try:
            db_primary_key = const.MAPPING_IDS[table_name]
            delete_data = "DELETE FROM %s where %s = %s" % (table_name,
                                                            db_primary_key, id)
            print("Deleting data", delete_data)
            self.cursor.execute(delete_data)
            self.conn.commit()
        except Exception as e:
            print(e)

    def search(self, data_l):
        try:
            contact_id_l = list()
            for data_s in data_l:
                for table in const.TABLES:
                    table_attr = table.upper() + '_ATTR'
                    search_elem = '%' + data_s + '%'
                    for attribute in const.MAPPING_TBL_ATTR.get(table_attr):
                        query = 'select ContactID from %s where %s LIKE "% s"' \
                                % (table, attribute, search_elem)
                        self.cursor.execute(query)
                        for data in self.cursor:
                            contact_id_l.append(str(data[0]))
            return list(set(contact_id_l))
        except Exception as e:
            print(e)

    def make_table(self, contact_id):
        try:
            table_data = dict()
            for table in const.TABLES:
                query = "select * from %s where ContactID = %s" % (table,
                                                                   contact_id)
                self.cursor.execute(query)
                data_l = list()
                for data in self.cursor:
                    data_l.append(list(data))
                table_data.update({table: data_l})
            return table_data
        except Exception as e:
            print(e)


if __name__ == "__main__":
    a = DBHandler()
    a.create_connect()
    b = DataManipulation(a)
    table_data = b.update_table_data()
    b.create_html(table_data)
    a.close_connect()

exit(0)
