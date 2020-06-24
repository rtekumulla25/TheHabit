from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from argon2 import PasswordHasher
from models import user_table
import hashlib

def createApp():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test.db'
    db = SQLAlchemy(app)
    return app, db

def isVerified(password):   #?????
    ph = PasswordHasher()
    hash = ph.hash("")   #password
    if ph.verify(hash, "") == True:
        pass
    else:
        pass


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def index():
    if request.method == 'POST':
        email_ent = request.form['email_login']
        password_ent = request.form['password_login']
        email_task = user_table(email=email_ent)
        hsh = hashlib.md5(password_ent.encode())
        password_task = user_table(pswd_hash=hsh)

        try:
            db.session.add(email_task)
            db.session.add(password_task)
            db.commit()
            return redirect('/')
        except:
            return 'there was an issue'
    else:
        tasks = user_table.query.all()
        return render_template('index.html', tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True)