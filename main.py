from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tqt46QaxU7dKz6fhDSsMQi3eEEU4CKyv'


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.form:
        print(list(request.form.values()))
    active = ['active', 'no', 'no', 'no', 'no', 'no', 'no']
    return render_template("home.html", active=active)

@app.route("/business")
def business():
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM business;")
    data = cur.fetchall()
    con.commit()
    con.close()
    active = ['no', 'active', 'no', 'no', 'no', 'no', 'no']
    return render_template("business.html", data=data, active=active)

@app.route("/users")
def users():
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users;")
    data = cur.fetchall()
    con.commit()
    con.close()
    active = ['no', 'no', 'active', 'no', 'no', 'no', 'no']
    return render_template("users.html", data=data, active=active)

@app.route("/reviews")
def reviews():
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM reviews;")
    data = cur.fetchall()
    con.commit()
    con.close()
    active = ['no', 'no', 'no', 'active', 'no', 'no', 'no']
    return render_template("reviews.html", data=data, active=active)

@app.route("/checkins")
def checkins():
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM checkins;")
    # data = cur.fetchall()
    data = cur.fetchmany(20)
    con.commit()
    con.close()
    active = ['no', 'no', 'no', 'no', 'active', 'no', 'no']
    return render_template("checkins.html", data=data, active=active)

@app.route("/sql")
def sql():
    active = ['no', 'no', 'no', 'no', 'no', 'active', 'no']
    return render_template("sql.html", active=active)

@app.route("/getdata")
def getdata():
    command = request.args.get("command")
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    cur.execute(command)
    data = cur.fetchall()
    con.commit()
    con.close()
    col = [description[0] for description in cur.description]
    return jsonify({"data":data, "col":col})

@app.route("/queries")
def queries():
    active = ['no', 'no', 'no', 'no', 'no', 'no', 'active']
    return render_template("queries.html", active=active)

@app.route('/delete_review/<string:id>', methods=['POST'])
def delete_review(id):
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    command = '''DELETE FROM reviews where rid = ?'''
    cur.execute(command, [id])
    con.commit()
    con.close()
    flash('Data Deleted', 'success')
    return redirect(url_for('reviews'))


@app.route('/delete_user/<string:id>', methods=['POST'])
def delete_user(id):
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    command = '''DELETE FROM users where uid = ?'''
    cur.execute(command, [id])
    con.commit()
    con.close()
    flash('Data Deleted', 'success')
    return redirect(url_for('users'))


@app.route('/delete_business/<string:id>', methods=['POST'])
def delete_business(id):
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    command = '''DELETE FROM business where bid = ?'''
    cur.execute(command, [id])
    con.commit()
    con.close()
    flash('Data Deleted', 'success')
    return redirect(url_for('business'))


@app.route('/delete_checkins/<string:id>', methods=['POST'])
def delete_checkins(id):
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    command = '''DELETE FROM checkins where bid = ?'''
    cur.execute(command, [id])
    con.commit()
    con.close()
    flash('Data Deleted', 'success')
    return redirect(url_for('checkins'))


@app.route('/update_reviews', methods=['POST'])
def update_reviews():
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    inputs = list(request.form.values())
    key = [inputs[0]]
    cur.execute('SELECT * from reviews WHERE rid = ?', key)
    if len(cur.fetchall()) == 0:
        command = '''INSERT INTO reviews VALUES (?,?,?,?,?)'''
        cur.execute(command, inputs)
        print('data inserted!')
        flash('Data inserted', 'success')

    else: # update row
        command = '''UPDATE reviews
                    SET rid = ?, bid = ?, uid = ?, stars = ?, text = ?
                    WHERE rid = ?;
                    '''
        cur.execute(command, inputs+key)
        print('data updated!')
        flash('Data updated', 'success')

    con.commit()
    con.close()
    return redirect(url_for('reviews'))


@app.route('/update_users', methods=['POST'])
def update_users():
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    command = '''INSERT INTO users VALUES (?,?,?,?)'''
    cur.execute(command, list(request.form.values()))
    con.commit()
    con.close()
    flash('Data inserted', 'success')
    return redirect(url_for('users'))


@app.route('/update_business', methods=['POST'])
def update_business():
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    command = '''INSERT INTO business VALUES (?,?,?,?,?,?)'''
    cur.execute(command, list(request.form.values()))
    con.commit()
    con.close()
    flash('Data inserted', 'success')
    return redirect(url_for('business'))


@app.route('/update_checkins', methods=['POST'])
def update_checkins():
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    command = '''INSERT INTO checkins VALUES (?,?,?,?,?,?,?,?)'''
    cur.execute(command, list(request.form.values()))
    con.commit()
    con.close()
    flash('Data inserted', 'success')
    return redirect(url_for('checkins'))

if __name__ == "__main__":
    app.run(debug=True)
