from Cheetah.Template import Template


class DataManipulation:
    def __init__(self, dbhandler_o):
        self.dbhandler_o = dbhandler_o

    def validate_form_data(self, form_data_d):
        try:
            errors = list()
            firstname = form_data_d.get('firstname', None)[0]
            middlename = form_data_d.get('middlename', None)[0]
            lastname = form_data_d.get('lastname', None)[0]
            address = form_data_d.get('address', None)
            address_type = form_data_d.get('address_type', None)
            city = form_data_d.get('city', None)
            zip_code = form_data_d.get('zip', None)
            state = form_data_d.get('state', None)
            date = form_data_d.get('date', None)
            datetype = form_data_d.get('datetype', None)
            areacode = form_data_d.get('areacode', None)
            ph_number = form_data_d.get('ph_number', None)
            phone_type = form_data_d.get('phone_type', None)
            name_query = '("%s","%s","%s")' % (firstname, middlename, lastname)
            for z in zip_code:
                if len(str(z)) != 5:
                    errors.append("Please check the Zip Code")
            for a in areacode:
                if len(str(a)) != 3:
                    errors.append("Please check the Area Code")
            for p in ph_number:
                if len(str(p)) != 7:
                    errors.append("Please check the Phone Number")
            if errors:
                return errors, False
            contact_id = self.dbhandler_o.create('CONTACT', name_query)
            for index in range(len(address_type)):
                if address[index]:
                    address_query = '(%s,"%s","%s","%s","%s",%s)' % (
                        contact_id, address_type[index], address[index],
                        city[index], state[index], zip_code[index])
                    self.dbhandler_o.create('ADDRESS', address_query)
            for index in range(len(phone_type)):
                if areacode[index]:
                    phone_query = '("%s",%s,%s,%s)' % (
                        phone_type[index], contact_id, areacode[index],
                        ph_number[index])
                    self.dbhandler_o.create('PHONE', phone_query)
            for index in range(len(datetype)):
                if date[index]:
                    date_query = '(%s,"%s","%s")' % (
                        contact_id, datetype[index], date[index])
                    self.dbhandler_o.create('DATE', date_query)
            return None, True
        except Exception as e:
            return [e], False

    def update_table_data(self, search_query=None):
        if search_query is None:
            search_query = ['a']
        contact_id_l = self.dbhandler_o.search(search_query)
        data_l = list()
        for d in contact_id_l:
            data_l.append(self.dbhandler_o.make_table(d))
        final_data = list()
        for elem in data_l:
            name = elem.get('CONTACT')[0]
            address = elem.get('ADDRESS')
            phone = elem.get('PHONE')
            date = elem.get('DATE')
            name = [str(n).replace('None', ' ') for n in name]
            ID = str(name[0])
            NAME = str(name[1]) + ' ' + str(name[2]) + ' ' + str(name[3])
            add_l = list()
            if address:
                for add in address:
                    a_id = add[0]
                    add_type = add[2]
                    ADDRESS = str(add[3]) + ', ' + str(add[4]) + ',' + str(
                        add[5])
                    if add[6] != 0:
                        ADDRESS = ADDRESS + '-' + str(add[6])
                    d = {'type': add_type, 'ADDRESS': ADDRESS, 'ID': a_id}
                    add_l.append(d)
            phone_l = list()
            if phone:
                for p in phone:
                    p_id = p[0]
                    phone_type = p[1]
                    number = '(' + str(p[3]) + ') ' + str(
                        p[4] // 10000) + '-' + str(p[4] % 10000)
                    d = {'type': phone_type, 'PHONE': number, 'ID': p_id}
                    phone_l.append(d)
            date_l = list()
            if date:
                for dt in date:
                    dt_id = dt[0]
                    date_type = dt[2]
                    dt_read = dt[3]
                    d = {'type': date_type, 'DATE': dt_read, 'ID': dt_id}
                    date_l.append(d)
            final_d = {'CONTACT': NAME, 'ADDRESS': add_l, 'PHONE': phone_l,
                       'DATE': date_l, 'ID': ID}
            final_data.append(final_d)
        return final_data

    def delete_record(self, id):
        try:
            self.dbhandler_o.delete('CONTACT', id)
            return None, True
        except Exception as e:
            return [e], False

    def create_html(self, table_data):
        write_file = open('templates/show.html', 'w+')
        templateDef = open('templates/table_template.html', 'r').read()
        t = Template(templateDef, searchList={'data_l': table_data})
        write_file.write(str(t))
        write_file.close()
