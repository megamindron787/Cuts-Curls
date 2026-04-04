from flask import Flask,url_for,render_template,redirect,request,session
import sqlite3
from database import appointment
import smtplib


appointment()

app = Flask(__name__)
app.secret_key = "hello123"

def send_email(email, name, service, date, time):
    sender_email = "ajinkyad537@gmail.com"
    sender_password = "wzqy xvsv cndy noij"
    receiver_email = email

    subject = "Appointment Confirmation"
    message = f"""Subject: {subject}

Dear {name},
Your appointment at Cuts & Curls has been successfully booked!
Here are your booking details:

    Service  : {service}
    Date     : {date}
    Time     : {time}

Please arrive 5 minutes before your scheduled time.
If you need to cancel or reschedule, contact us at least 24 hours in advance.

Thank you for choosing Cuts & Curls!

Warm regards,
The Cuts & Curls Team
"""

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()


        
@app.route('/skincare')
def skincare():
    return render_template('skincare.html')

@app.route('/haircare')
def haircare():
    return render_template('haircare.html')

@app.route('/male-hairstyle')
def male_hairstyle():
    return render_template('male-hairstyle.html')

@app.route('/female-hairstyle')
def female_hairstyle():
    return render_template('female-hairstyle.html')



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/booking', methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        gender = request.form.get('gender')
        service = request.form.get('service')
        date = request.form.get('date')
        time = request.form.get('time') 

        conn = sqlite3.connect('appointment.db')
        cur = conn.cursor()

        cur.execute("""INSERT INTO appointments(name,email,mobile,gender,service,date,time)
                    VALUES(?,?,?,?,?,?,?)""",
                    (name,email,mobile,gender,service,date,time))
        conn.commit()
        conn.close()               
        
        send_email(email,name,service,date,time)
        return redirect('/')

    return render_template('booking.html')


if __name__ == '__main__':
    app.run(debug=True)

    