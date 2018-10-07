from Cheetah.Template import Template


class DataManipulation:
    def __init__(self, dbhandler_o):
        self.dbhandler_o = dbhandler_o

    def validate_form_data(self, form_data_d):
        try:
            errors = list()
            zip_code = form_data_d.get('zip', None)
            areacode = form_data_d.get('areacode', None)
            ph_number = form_data_d.get('ph_number', None)
            for z in zip_code:
                if z:
                    if len(str(z)) != 5:
                        errors.append("Please check the Zip Code %s" % z)
            for a in areacode:
                if a:
                    if a and len(str(a)) != 3:
                        errors.append("Please check the Area Code %s" % a)
            for p in ph_number:
                if p:
                    if p and len(str(p)) != 7:
                        errors.append("Please check the Phone Number %s" % p)
            if errors:
                return errors
            return None
        except Exception as e:
            return [e], False

    def create_data(self, form_data_d):
        errors = self.validate_form_data(form_data_d)
        if errors:
            return errors, False
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

    def update_data(self, form_data_d):
        contact_id = form_data_d['contact_id'][0]
        old_data = self.dbhandler_o.make_table(contact_id)
        errors = self.validate_form_data(form_data_d)
        if errors:
            return errors, False
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
        name_query = 'Fname="%s",Mname="%s",Lname="%s"' % (
            firstname, middlename, lastname)
        self.dbhandler_o.update('CONTACT', contact_id, name_query)
        old_add_id, old_ph_id, old_dt_id = [], [], []
        for add in old_data['ADDRESS']:
            old_add_id.append(add[0])
        for phone in old_data['PHONE']:
            old_ph_id.append(phone[0])
        for date in old_data['DATE']:
            old_dt_id.append(date[0])
        for index in range(len(form_data_d['add_id'])):
            add_id = int(form_data_d['add_id'][index])
            if address[index]:
                if add_id == 0:
                    address_query = '(%s,"%s","%s","%s","%s",%s)' % (
                        contact_id, address_type[index], address[index],
                        city[index], state[index], zip_code[index])
                    self.dbhandler_o.create('ADDRESS', address_query)
                elif add_id not in old_add_id:
                    self.dbhandler_o.delete('ADDRESS', add_id)
                else:
                    address_query = 'Address_type="%s", Address="%s", ' \
                                    'City="%s", State="%s", Zip=%s' % (
                                        address_type[index], address[index],
                                        city[index], state[index],
                                        zip_code[index])
                    self.dbhandler_o.update('ADDRESS', add_id, address_query)

        for index in range(len(form_data_d['ph_id'])):
            ph_id = int(form_data_d['ph_id'][index])
            if ph_number[index]:
                if ph_id == 0:
                    phone_query = '("%s",%s,%s,%s)' % (
                        phone_type[index], contact_id, areacode[index],
                        ph_number[index])
                    self.dbhandler_o.create('PHONE', phone_query)
                elif ph_id not in old_add_id:
                    self.dbhandler_o.delete('PHONE', ph_id)
                else:
                    phone_query = 'PhoneType="%s",AreaCode=%s,Number=%s' % (
                        phone_type[index], areacode[index], ph_number[index])
                    self.dbhandler_o.update('PHONE', ph_id, phone_query)

        for index in range(len(form_data_d['dt_id'])):
            dt_id = int(form_data_d['dt_id'][index])
            if date[index]:
                if dt_id == 0:
                    date_query = '(%s,"%s","%s")' % (
                        contact_id, datetype[index], date[index])
                    self.dbhandler_o.create('DATE', date_query)
                elif dt_id not in old_add_id:
                    self.dbhandler_o.delete('DATE', dt_id)
                else:
                    date_query = 'DateType="%s",Date="%s"' % (
                        datetype[index], date[index])
                    self.dbhandler_o.update('DATE', dt_id, date_query)

        return None, True

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

    def create_html(self, filename, template, table_data):
        file_path = 'templates/' + filename
        template_path = 'templates/' + template
        write_file = open(file_path, 'w+')
        templateDef = open(template_path, 'r').read()
        t = Template(templateDef, searchList={'data_l': table_data})
        write_file.write(str(t))
        write_file.close()
