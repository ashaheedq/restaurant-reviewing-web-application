from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from db_manager import update_, sql_command

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tqt46QaxU7dKz6fhDSsMQi3eEEU4CKyv'


@app.route("/", methods=['GET', 'POST'])
def home():
    active = ['active', 'no', 'no', 'no', 'no', 'no', 'no']
    return render_template("home.html", active=active)


@app.route("/business")
def business():
    data, _ = sql_command("SELECT * FROM business;")
    active = ['no', 'active', 'no', 'no', 'no', 'no', 'no']
    return render_template("business.html", data=data, active=active)


@app.route("/users")
def users():
    data, _ = sql_command("SELECT * FROM users;")
    active = ['no', 'no', 'active', 'no', 'no', 'no', 'no']
    return render_template("users.html", data=data, active=active)


@app.route("/reviews")
def reviews():
    data, _ = sql_command("SELECT * FROM reviews;")
    active = ['no', 'no', 'no', 'active', 'no', 'no', 'no']
    return render_template("reviews.html", data=data, active=active)


@app.route("/checkins")
def checkins():
    data, _ = sql_command("SELECT * FROM checkins;")
    active = ['no', 'no', 'no', 'no', 'active', 'no', 'no']
    return render_template("checkins.html", data=data, active=active)


@app.route("/sql")
def sql():
    active = ['no', 'no', 'no', 'no', 'no', 'active', 'no']
    return render_template("sql.html", active=active)


@app.route("/getdata")
def getdata():
    command = request.args.get("command")
    data, col = sql_command(command)
    return jsonify({"data": data, "col": col})


@app.route("/queries")
def queries():
    active = ['no', 'no', 'no', 'no', 'no', 'no', 'active']
    return render_template("queries.html", active=active)


@app.route('/delete_review/<string:id>', methods=['POST'])
def delete_review(id):
    command = '''DELETE FROM reviews where rid = ?'''
    update_(command, [id])
    flash('Data Deleted', 'success')
    return redirect(url_for('reviews'))


@app.route('/delete_user/<string:id>', methods=['POST'])
def delete_user(id):
    command = '''DELETE FROM users where uid = ?'''
    update_(command, [id])
    flash('Data Deleted', 'success')
    return redirect(url_for('users'))


@app.route('/delete_business/<string:id>', methods=['POST'])
def delete_business(id):
    command = '''DELETE FROM business where bid = ?'''
    update_(command, [id])
    flash('Data Deleted', 'success')
    return redirect(url_for('business'))


@app.route('/delete_checkins/<string:id>', methods=['POST'])
def delete_checkins(id):
    command = '''DELETE FROM checkins where bid = ?'''
    update_(command, [id])
    flash('Data Deleted', 'success')
    return redirect(url_for('checkins'))


@app.route('/update_reviews', methods=['POST'])
def update_reviews():
    inputs = list(request.form.values())
    key = [inputs[0]]
    data, _ = sql_command('SELECT * from reviews WHERE rid = ?', key)
    if len(data) == 0:
        command = '''INSERT INTO reviews VALUES (?,?,?,?,?)'''
        update_(command, inputs)
        print('data inserted!')
        flash('Data inserted', 'success')

    else:  # update row
        command = '''UPDATE reviews
                    SET rid = ?, bid = ?, uid = ?, stars = ?, text = ?
                    WHERE rid = ?;
                    '''
        update_(command, inputs+key)
        print('data updated!')
        flash('Data updated', 'success')

    return redirect(url_for('reviews'))


@app.route('/update_users', methods=['POST'])
def update_users():

    inputs = list(request.form.values())
    key = [inputs[0]]
    data, _ = sql_command('SELECT * from business WHERE bid = ?', key)

    if len(data) == 0:
        command = '''INSERT INTO users VALUES (?,?,?,?)'''
        update_(command, inputs)
        print('data inserted!')
        flash('Data inserted', 'success')

    else:  # update row
        command = '''UPDATE users
                    SET uid = ?, uname = ?, review_count = ?, avg_stars = ?
                    WHERE uid = ?;
                '''
        update_(command, inputs+key)
        print('data updated!')
        flash('Data updated', 'success')

    return redirect(url_for('users'))


@app.route('/update_business', methods=['POST'])
def update_business():
    inputs = list(request.form.values())
    key = [inputs[0]]
    data, _ = sql_command('SELECT * from business WHERE bid = ?', key)

    if len(data) == 0:
        command = '''INSERT INTO business VALUES (?,?,?,?,?,?)'''
        update_(command, inputs)
        print('data inserted!')
        flash('Data inserted', 'success')

    else:  # update row
        command = '''UPDATE business
                    SET bid = ?, bname = ?, categories = ?, active = ?, review_count = ?, stars = ?
                    WHERE bid = ?;
                    '''
        update_(command, inputs+key)
        print('data updated!')
        flash('Data updated', 'success')

    return redirect(url_for('business'))


@app.route('/update_checkins', methods=['POST'])
def update_checkins():
    inputs = list(request.form.values())
    key = [inputs[0]]
    data, _ = sql_command('SELECT * from checkins WHERE bid = ?', key)

    if len(data) == 0:
        command = '''INSERT INTO checkins VALUES (?,?,?,?,?,?,?,?)'''
        update_(command, inputs)
        print('data inserted!')
        flash('Data inserted', 'success')

    else:  # update row
        command = '''UPDATE checkins
                    SET bid = ?, Sunday = ?, Monday = ?, Tuesday = ?, Wednesday = ?, Thursday = ?, Friday = ?, Saturday = ?
                    WHERE bid = ?;
                    '''
        update_(command, inputs+key)
        print('data updated!')
        flash('Data updated', 'success')

    return redirect(url_for('checkins'))


if __name__ == "__main__":
    app.run(debug=True)
