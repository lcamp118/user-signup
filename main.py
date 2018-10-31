from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('form.html', username='', email='')

@app.route('/', methods=["POST"])
def errors():
    username = request.form['username']
    password = request.form['password']
    confirm = request.form['confirm']
    email = request.form['email']
   
    username_error = ''
    password_error = ''
    confirm_error = ''
    email_error = ''

    invalid_char = ' '
   
    if len(username) < 3 or len(username) > 20:
        username_error = "Username must be between 3-20 characters in length"
    elif not username == "":
        username = username
    if len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3-20 characters in length"
    if password != confirm:
        confirm_error = "Passwords must match"
    for char in username:
        if char in invalid_char:
            username_error = "Username cannot contain spaces"
    for char in password:
        if char in invalid_char:
            password_error = "Password cannot contain spaces"
    
    if not email:
        email=""
        email_error=""
    else:
        if len(email) < 3 or len(email) > 20:
            email_error = "Please enter a valid email address"
        else:
            if ' ' in email:
                email_error = "Email address cannot contain spaces"
            else:
                if '@' not in email:
                    email_error = "Please enter a valid email address"
                else:
                    if '.' not in email:
                        email_error = "Please enter a valid email address"
   
    if username_error == "" and password_error == "" and confirm_error == "" and email_error == "":
        username = username
        return redirect('/welcome?username={0}'.format(username))
   
    else:
        return render_template('form.html',username_error=username_error, password_error=password_error, confirm_error=confirm_error, email_error = email_error, username=username, email=email)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()