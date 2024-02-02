from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('SSLform.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Fetching form data
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

        # Process the form data as required
        
        # For now, just printing the data to console
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Email:", email)
        print("Phone Number:", phone_number)
        print("Address:", address)
        print("City:", city)
        print("State:", state)
        print("Postal Code:", postal_code)
        print("Check-in Date:", check_in_date)
        print("Check-out Date:", check_out_date)
        print("Room Type:", room_type)
        print("Number of Guests:", num_guests)
        print("Notes:", notes)

        return 'Form submitted successfully'

if __name__ == '__main__':
    app.run(debug=True)
