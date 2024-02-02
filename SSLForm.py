from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('SSLForm.html')


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        street_address = request.form['street_address']
        city = request.form['city']
        province = request.form['province']
        postal_code = request.form['postal_code']
        check_in_date = request.form['check_in_date']
        check_out_date = request.form['check_out_date']
        room_type = request.form['room_type']
        num_guests = request.form['num_guests']
        optional_notes = request.form['optional_notes']

        # Here you can process the form data as per your requirements

        return render_template('success.html', 
                               first_name=first_name, 
                               last_name=last_name, 
                               email=email,
                               phone_number=phone_number,
                               street_address=street_address,
                               city=city,
                               province=province,
                               postal_code=postal_code,
                               check_in_date=check_in_date,
                               check_out_date=check_out_date,
                               room_type=room_type,
                               num_guests=num_guests,
                               optional_notes=optional_notes)
    return 'Something went wrong!'

if __name__ == '__main__':
    app.run(debug=True)
