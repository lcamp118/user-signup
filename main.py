from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('form.html')

@app.route('/validate')
def validate():
    username = request.args.get['username']
    if username == "":
        username-error = "Please enter a valid username"
        return username-error
    if password == "":
        return "Please Enter A Valid Password"
    if confirm == "":
        return "Please Re-Enter Password"

app.run()