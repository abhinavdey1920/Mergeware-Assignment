from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
users = []
loans = []
payments = []
roles = ['admin', 'borrower', 'lender']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        role = request.form.get('role')
        users.append({'email': email, 'role': role})
        return redirect(url_for('dashboard', email=email))
    return render_template('register.html', roles=roles)

@app.route('/dashboard/<email>')
def dashboard(email):
    user = next((u for u in users if u['email'] == email), None)
    return render_template('dashboard.html', user=user, loans=loans, payments=payments)

@app.route('/request_loan/<email>')
def request_loan(email):
    loans.append({'borrower': email, 'status': 'pending'})
    return redirect(url_for('dashboard', email=email))

@app.route('/confirm_payment/<email>')
def confirm_payment(email):
    payments.append({'lender': email, 'status': 'confirmed'})
    return redirect(url_for('dashboard', email=email))

if __name__ == '__main__':
    app.run(debug=True)

# app.py

# ... (other code)

@app.route('/')
def index():
    return render_template('index.html')


# app.py

# ... (other code)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        role = request.form.get('role')
        users.append({'email': email, 'role': role})
        return redirect(url_for('dashboard', email=email))
    return render_template('register.html', roles=roles)


# app.py

# ... (other code)

@app.route('/dashboard/<email>')
def dashboard(email):
    user = next((u for u in users if u['email'] == email), None)
    return render_template('dashboard.html', user=user, loans=loans, payments=payments)


