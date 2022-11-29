import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
app.secret_key = os.environ.get("WTF_SECRET")
Bootstrap(app)


class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[InputRequired(), Email(message="Nope")])
    password = PasswordField(label='password', validators=[InputRequired(), Length(message="not long enough", min=8)])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
