from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Preset username and password
preset_username = "Krish B"
preset_password = "123456"

# Mock database for demonstration
users = [
    {'account_number': '123456', 'pin': '123456', 'name': 'Krish B', 'balance': 1000},
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


@app.route('/modify-account', methods=['GET', 'POST'])
def modify_account():
    # Assuming user is logged in and modifying their own account
    user = users[0]  # Assuming the first user in the list is logged in

    if request.method == 'POST':
        new_name = request.form['name']
        new_pin = request.form['newPin']
        # Update user data in the mock database
        user['name'] = new_name
        user['pin'] = new_pin
        # Redirect to dashboard after saving changes
        return redirect(url_for('dashboard'))

    return render_template('modify_account.html', user=user)


    return render_template('modify_account.html', user=user)
@app.route('/logout')
def logout():
    # Clear session or any other logout logic
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
