from flask import render_template, request, redirect, url_for

from application import app, db
from application.comments.models import Comment
from application.comments.forms import CommentForm
from flask_login import login_required, current_user
from application.matches.models import Match

@app.route("/comments/<match_id>/")
def comments_form(match_id):
    return render_template("comments/list.html", form = CommentForm(), matches = Match.query.filter_by(id=match_id), comments = Comment.query.filter_by(matchid=match_id))

@app.route("/comments/<matchID>/", methods=["POST"])
@login_required
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