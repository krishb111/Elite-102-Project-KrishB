from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configure static files (CSS, JavaScript, etc.)
app.static_folder = 'static'

# Database Initialization
conn = sqlite3.connect('bank_database.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY,
        account_number INTEGER UNIQUE,
        pin INTEGER,
        name TEXT,
        balance REAL DEFAULT 0
    )
''')
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        name = request.form['name']
        account_number = request.form['account_number']
        pin = request.form['pin']

        conn = sqlite3.connect('bank_database.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO accounts (name, account_number, pin) VALUES (?, ?, ?)', (name, account_number, pin))
            conn.commit()
        except sqlite3.IntegrityError as e:
            print("Error: Account number already exists.")
            conn.rollback() 
        finally:
            conn.close()

        return redirect(url_for('index'))
    return render_template('create_account.html')

@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session:
        user_name = "Krish B"  
        account_number = "123456"  
        balance = 5000.00  
        return render_template('dashboard.html', user_name=user_name, account_number=account_number, balance=balance)
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
