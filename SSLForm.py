from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('SSLform.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
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

        return 'Form submitted successfully'

if __name__ == '__main__':
    app.run(debug=True)
