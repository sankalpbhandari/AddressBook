#!/usr/bin/python
from flask import Flask, render_template, request, redirect

from AddressBook.data.data_manipulation import DataManipulation
from AddressBook.handlers.db_handler import DBHandler

app = Flask(__name__)
app.secret_key = b'MyAddressBook'

dbhandler_o = DBHandler()
conn = dbhandler_o.create_connect()
data_m_o = DataManipulation(dbhandler_o)


@app.route("/", methods=["POST"])
def createtable():
    search_query = request.form.get('search', None)
    search_l = search_query.split(" ")
    table_data = data_m_o.update_table_data(search_l)
    data_m_o.create_html(table_data)
    return redirect('/')


@app.route("/", methods=["GET"])
def showtable():
    message = None
    return render_template("show.html", messages=message)


@app.route("/contact_form.html", methods=["GET", "POST"])
def contact_form():
    errors = None
    if request.method == 'POST':
        contact_form_d = dict(request.form)
        errors, success = data_m_o.validate_form_data(contact_form_d)
        if success:
            return redirect('/')
    return render_template("contact_form.html", errors=errors)


if __name__ == '__main__':
    try:
        table_data = data_m_o.update_table_data()
        data_m_o.create_html(table_data)
        app.config['TEMPLATES_AUTO_RELOAD'] = True
        app.run()
    except Exception as e:
        print e
