from flask import Flask, render_template, request, jsonify, redirect, url_for
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

cursor = db_connection.cursor(dictionary=True)


@app.route('/')
def index():
    return render_template('elechome.html')

@app.route('/home')
def home():
    return render_template('elechome.html')

@app.route('/showRoomCase')
def showRoomCase():
    return render_template('RoomShowcase.html')

@app.route('/room1')
def room1():
    return render_template('ViewRoom1.html')

@app.route('/room2')
def room2():
    return render_template('ViewRoom2.html')

@app.route('/room3')
def room3():
    return render_template('ViewRoom3.html')

@app.route('/checkout')
def checkout():
    cursor.execute("SELECT * FROM sereneform")
    checkouts = cursor.fetchall()
    return render_template('checkout.html',checkouts=checkouts)

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        email = request.form['emailDelete']
        check_in_date = request.form['checkinDelete']
        check_out_date = request.form['checkoutDelete']
        room_type = request.form['roomDelete']
        
        cursor.execute("DELETE FROM sereneform WHERE email = %s AND checkin = %s AND checkout = %s AND room = %s", (email, check_in_date, check_out_date, room_type))
        db_connection.commit()
        
        return redirect(url_for('checkout'))
    return render_template('checkout.html')


@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form['fnames']
        email = request.form['mails']
        message = request.form['notes']
        
        cursor.execute("INSERT INTO contact (name,email,message) VALUES (%s,%s,%s)",(name,email,message))
        db_connection.commit()
        
        msg_Feedback = Message('Thank you for contacting us', recipients=[email])
        msg_Feedback.body = f"Dear {name},\n\nThank you for booking."
        mail.send(msg_Feedback)
        
    return render_template('contact.html')

@app.route('/sslform', methods=['GET', 'POST'])
def sslform():
    if request.method == 'POST':
        check_in_date = request.form['cndcalendar']
        check_out_date = request.form['codcalendar']
        room_type = request.form['room']
        
        cursor.execute("SELECT * FROM sereneform WHERE room = %s AND checkin <= %s AND checkout >= %s", (room_type, check_out_date, check_in_date))
        conflict = cursor.fetchall()
        
        if conflict:
            return jsonify({'error': 'Another booking exists for the same room.'}), 400
        else:
            first_name = request.form['fnames']
            last_name = request.form['lnames']
            email = request.form['mailes']
            phone_number = request.form['numbers']
            address = request.form['addre']
            city = request.form['cits']
            state = request.form['stats']
            postal_code = request.form['postals']
            num_guests = request.form['numguest']
            notes = request.form['nots']

            cursor.execute("INSERT INTO sereneform (fname, lname, email, phone, address, city, state, postal, checkin, checkout, room, guests, notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (first_name, last_name, email, phone_number, address, city, state, postal_code, check_in_date, check_out_date, room_type, num_guests, notes))
            
            msg_Feedback = Message('Thank you for your booking', recipients=[email])
            msg_Feedback.body = f"Dear {first_name},\n\nThank you for booking."
            mail.send(msg_Feedback)

            db_connection.commit()

            return render_template('elechome.html')
    
    return jsonify({'error': 'Invalid Request'}), 400
    
if __name__ == '__main__':
    app.run(debug=True)
