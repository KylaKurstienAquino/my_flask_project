from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'serene_skyline'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('SSLform.html')

@app.route('/sslform', methods=['GET','POST'])
def sslform():
    if request.method == 'POST':
        first_name = request.form['fnames']
        last_name = request.form['lnames']
        email = request.form['mailes']
        phone_number = request.form['numbers']
        address = request.form['addre']
        city = request.form['cits']
        state = request.form['stats']
        postal_code = request.form['postals']
        check_in_date = request.form['cndcalendar']
        check_out_date = request.form['codcalendar']
        room_type = request.form['room']
        num_guests = request.form['numguest']
        notes = request.form['numguest']

        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO your_table (first_name, last_name, email, phone_number, address, city, state, postal_code, check_in_date, check_out_date, room_type, num_guests, notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (first_name, last_name, email, phone_number, address, city, state, postal_code, check_in_date, check_out_date, room_type, num_guests, notes))
            mysql.connection.commit()
            cur.close()
            return 'Form submitted successfully'
        except Exception as e:
            return f"An error occurred: {str(e)}"
        
        return render_template('elechome.html')
    
if __name__ == '__main__':
    app.run(debug=True)
