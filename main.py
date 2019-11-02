from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.form:
        print(request.form)
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
    # data = cur.fetchmany(20)
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
    data = cur.fetchall()
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
    col = [description[0] for description in cur.description]
    return jsonify({"data":data, "col":col})

@app.route("/queries")
def queries():
    active = ['no', 'no', 'no', 'no', 'no', 'no', 'active']
    return render_template("queries.html", active=active)

if __name__ == "__main__":
    app.run(debug=True)
