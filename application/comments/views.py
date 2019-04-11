from flask import render_template, request, redirect, url_for

from application import app, db, login_required
from application.comments.models import Comment
from application.comments.forms import CommentForm
from flask_login import current_user
from application.matches.models import Match

@app.route("/comments/<match_id>/")
def comments_form(match_id):
    return render_template("comments/list.html", form = CommentForm(), matches = Match.query.filter_by(id=match_id), comments = Comment.query.filter_by(matchid=match_id))

@app.route("/comments/<matchID>/", methods=["POST"])
@login_required(role="ANY")
def comments_create(matchID):
    form = CommentForm(request.form)

    if not form.validate():
        return render_template("comments/list.html", form = form, matches = Match.query.filter_by(id=matchID), comments = Comment.query.filter_by(matchid=matchID))

    c = Comment(form.content.data, matchID)
    c.account_id = current_user.id
    c.name = current_user.username
    db.session().add(c)
    db.session().commit()
    return render_template("comments/list.html", form = form, matches = Match.query.filter_by(id=matchID), comments = Comment.query.filter_by(matchid=matchID))

@app.route("/comments/<ID>, <matchId>/", methods=["POST"])
def comments_delete(ID, matchId):
    form = CommentForm(request.form)
    
    c = Comment.query.get(ID)
    db.session.delete(c)
    db.session.commit()
    return render_template("comments/list.html", form = form, matches = Match.query.filter_by(id=matchId), comments = Comment.query.filter_by(matchid=matchId))