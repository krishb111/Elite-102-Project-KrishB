from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Preset username and password
preset_username = "Krish B"
preset_password = "123456"

# Mock database for demonstration
users = [
    {'account_number': '123456', 'pin': '1234', 'name': 'John Doe', 'balance': 1000},
    {'account_number': '987654', 'pin': '4321', 'name': 'Jane Smith', 'balance': 500},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == preset_username and password == preset_password:
        # Redirect to dashboard if login is successful
        return redirect(url_for('dashboard'))
    else:
        return render_template('index.html', error=True)

@app.route('/dashboard')
def dashboard():
    # You can pass user data to the dashboard template
    # For demonstration purposes, let's assume the user is logged in
    user = users[0]  # Assuming the first user in the list is logged in
    return render_template('dashboard.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
