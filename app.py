
from flask import Flask, request, render_template, request, redirect, url_for,session
from flask_socketio import SocketIO
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os
import pandas as pd
import shutil
from predictions import *
from plots import *

app = Flask(__name__)
socketio = SocketIO(app)
#--------------------------------------------------------LOGIN----------------------------------------------------------------------------
app.secret_key = 'xyzsdfg'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'patient-details-system' # Replace with your MySQL database name
app.config['MYSQL_PORT'] = 3308  # Replace with your MySQL port
table_name = 'user' # Change this according to your database table name
mysql = MySQL(app)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'phone' in request.form and 'password' in request.form:
        phone = request.form['phone']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(f'SELECT * FROM {table_name} WHERE phone = %s AND password = %s', (phone, password,))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['phone'] = user['phone']
            session['password'] = user['password']
            message = 'Logged in successfully!'
            return render_template('upload.html', message=message)
        else:
            message = 'Please enter correct email / password!'
    return render_template('login.html', message=message)

# @app.route('/logout')
# def logout():
#     session.pop('loggedin', None)
#     session.pop('userid', None)
#     session.pop('phone', None)
#     return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'phone' in request.form and 'address' in request.form:
        userName = request.form['name']
        password = request.form['password']
        phone = request.form['phone']
        address = request.form['address']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        try:
            
            cursor.execute(f'INSERT INTO {table_name} (`name`, `phone`,`address`, `password`) VALUES (%s, %s,%s, %s)', (userName, phone,address, password,))
            mysql.connection.commit()
            message = 'You have successfully registered!'
            return redirect(url_for('login'))
        except MySQLdb.Error as e:
            print("MySQL Error during registration:", e)
            mysql.connection.rollback()  # Rollback in case of an error
            message = 'An error occurred during registration.'

    elif request.method == 'POST':
        message = 'Please fill out the form!'

    return render_template('register.html', message=message)

UPLOAD_FOLDER = 'uploads'
PLOT_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def process_files():
    
    save_predictions_csv()
    root = os.getcwd()
    pred_folder = os.path.join(root, 'Pred')
    csv_data_path = os.path.join(pred_folder , 'predictions.csv')
    global csv_data 
    csv_data = pd.read_csv(csv_data_path)
    
    plot_multiple_plots()

@app.route('/upload', methods=['POST'])
def upload_files():
    if request.method == 'POST':
        if 'csvFile' in request.files and 'axialFile' in request.files and 'coronalFile' in request.files and 'meniscusFile' in request.files:
            csv_file = request.files['csvFile']
            axial_file = request.files['axialFile']
            coronal_file = request.files['coronalFile']
            meniscus_file = request.files['meniscusFile']
            if csv_file.filename == '' or axial_file.filename == '' or coronal_file.filename == '' or meniscus_file.filename == '':
                return 'No selected file'
            if csv_file and axial_file and coronal_file and meniscus_file:
                # Remove existing uploads directory if it exists
                if os.path.exists(app.config['UPLOAD_FOLDER']):
                    shutil.rmtree(app.config['UPLOAD_FOLDER'])
                # Create a new uploads directory
                os.makedirs(app.config['UPLOAD_FOLDER'])

                csv_filename = 'blank_csv.csv'
                axial_filename = 'axial_numpy.npy'
                coronal_filename = 'coronal_numpy.npy'
                sagittal_filename = 'sagittal_numpy.npy'
                csv_file.save(os.path.join(app.config['UPLOAD_FOLDER'], csv_filename))
                axial_file.save(os.path.join(app.config['UPLOAD_FOLDER'], axial_filename))
                coronal_file.save(os.path.join(app.config['UPLOAD_FOLDER'], coronal_filename))
                meniscus_file.save(os.path.join(app.config['UPLOAD_FOLDER'], sagittal_filename))
                
                
                # Process files
                process_files()
                
                return render_template('result.html', csv_data=csv_data.to_html(), plot_path=os.path.join(PLOT_FOLDER, 'predictions_plot.png'))
    return 'Error uploading files'

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5000, debug=True, allow_unsafe_werkzeug=True)
