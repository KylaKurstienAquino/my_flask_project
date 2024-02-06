from flask import Flask, render_template, request
import mysql.connector
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kylakurstienaquino@gmail.com'
app.config['MAIL_PASSWORD'] = 'fiaq ebpy wyos aqdv'
app.config['MAIL_DEFAULT_SENDER'] = 'kylakurstienaquino@gmail.com'

mail = Mail(app)


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'serene_skyline'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

db_connection = mysql.connector.connect(
    host=app.config['MYSQL_DATABASE_HOST'],
    user=app.config['MYSQL_DATABASE_USER'],
    password=app.config['MYSQL_DATABASE_PASSWORD'],
    database=app.config['MYSQL_DATABASE_DB']
)

# Create a cursor to interact with the database
cursor = db_connection.cursor(dictionary=True)


@app.route('/')
def index():
    return render_template('elechome.html')

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
        notes = request.form['nots']

        cursor.execute("INSERT INTO sereneform (fname, lname, email, phone, address, city, state, postal, checkin, checkout, room, guests, notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (first_name, last_name, email, phone_number, address, city, state, postal_code, check_in_date, check_out_date, room_type, num_guests, notes))
        
        msg_Feedback = Message('Thank you for your booking', recipients=[email])
        msg_Feedback.body = f"Dear {first_name},\n\n thank you for booking"
        mail.send(msg_Feedback)

        db_connection.commit()


        return render_template('elechome.html')
    
if __name__ == '__main__':
    app.run(debug=True)
