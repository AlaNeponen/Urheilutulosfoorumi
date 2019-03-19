from application import app, db
from flask import redirect, render_template, request, url_for
from application.matches.models import Match
import datetime

@app.route("/matches", methods=["GET"])
def matches_index():
    return render_template("matches/list.html", matches = Match.query.all())

@app.route("/matches/new/")
def matches_form():
    return render_template("matches/new.html")

@app.route("/matches/", methods=["POST"])
def matches_create():
    date_str = request.form.get("date_when")
    date_time = datetime.datetime.strptime(date_str, '%d %m %Y')
    m = Match(request.form.get("winner"), request.form.get("opponent"), date_time, request.form.get("score"), request.form.get("event"))

    db.session().add(m)
    db.session().commit()

    return redirect(url_for("matches_index"))