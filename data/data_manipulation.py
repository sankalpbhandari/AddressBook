from Cheetah.Template import Template


class DataManipulation:
    def __init__(self, dbhandler_o):
        self.dbhandler_o = dbhandler_o

    def update_table_data(self):
        data = self.dbhandler_o.search(['Delinda', 'Hill'])
        data_l = list()
        for d in data:
            data_l.append(self.dbhandler_o.make_table(d))
        final_data = list()
        for elem in data_l:
            name = elem.get('CONTACT')[0]
            address = elem.get('ADDRESS')
            phone = elem.get('PHONE')
            date = elem.get('DATE')
            name = [str(n).replace('None', ' ') for n in name]
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
                       'DATE': date_l}
            final_data.append(final_d)
        return final_data

    def create_html(self, table_data):
        write_file = open('show.html', 'w+')
        templateDef = open('table_template.html', 'r').read()
        t = Template(templateDef, searchList={'data_l': table_data})
        write_file.write(str(t))
        write_file.close()