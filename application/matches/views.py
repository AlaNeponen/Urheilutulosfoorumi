from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user
from application.matches.models import Match
from application.matches.forms import MatchForm
from application.comments.models import Comment
import datetime

@app.route("/matches", methods=["GET"])
def matches_index():
    return render_template("matches/list.html", matches = Match.query.all())

@app.route("/matches/new/")
@login_required(role="ANY")
def matches_form():
    return render_template("matches/new.html", form = MatchForm())

@app.route("/matches/", methods=["POST"])
@login_required(role="ANY")
def matches_create():
    form = MatchForm(request.form)

    if not form.validate():
        return render_template("matches/new.html", form = form)

    date_str = (form.date_when.data)
    date_time = datetime.datetime.strptime(date_str, '%d %m %Y')
    m = Match(form.winner.data, form.opponent.data, date_time, form.score.data, form.event.data)
    m.account_id = current_user.id

    db.session().add(m)
    db.session().commit()

    return redirect(url_for("matches_index"))

@app.route("/matches/<match_ID>/", methods=["POST"])
@login_required(role="ANY")
def matches_delete(match_ID):
    matches = Match.query.filter_by(id=match_ID)
    for match in matches:
        match_comments = Comment.query.filter_by(matchid=match.id)
        for comment in match_comments:
            db.session.delete(comment)
        db.session.delete(match)
    db.session.commit()

    return redirect(url_for("matches_index"))