from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from application.matches.models import Match
from application.comments.models import Comment
from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/my_account")
@login_required(role="ANY")
def auth_own():
    return render_template("auth/my.html", matches = Match.query.filter_by(account_id=current_user.id))

@app.route("/auth/update_username")
def auth_updateName():
    return render_template("auth/username.html", form = LoginForm())

@app.route("/auth/update_password")
def auth_updatePassword():
    return render_template("auth/password.html", form = LoginForm())

@app.route("/auth/password", methods=["POST"])
def auth_password():
    form = LoginForm(request.form)
    u = User.query.get(current_user.id)
    u.password = form.password.data
    db.session.commit()
    flash("Password successfully updated!")
    return render_template("auth/my.html", matches = Match.query.filter_by(account_id=current_user.id))

@app.route("/auth/username", methods=["POST"])
def auth_username():
    form = LoginForm(request.form)
    users = User.query.all()
    for user in users:
        if user.username == form.username.data:
            flash("Username is already taken :'(")
            return render_template("auth/username.html", form = form)
    u = User.query.get(current_user.id)
    u.username = form.username.data
    db.session.commit()
    flash("Username successfully updated!")
    return render_template("auth/my.html", matches = Match.query.filter_by(account_id=current_user.id))


@app.route("/auth", methods=["GET" ,"POST"])
def auth_create():
    form = LoginForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)

    u = User(form.username.data, form.password.data, "PLEB")
    users = User.query.all()
    for user in users:
        if user.username == form.username.data:
            flash("Username is already taken :'(")
            return render_template("auth/new.html", form = form)

    db.session().add(u)
    db.session().commit()
    flash("Account created! :3")
    login_user(u)
    return redirect(url_for("index"))

@app.route("/auth/delete_user")
def auth_deleteUser():
    return render_template("auth/delete.html")

@app.route("/auth/delete", methods=["POST"])
def auth_delete():
    u = User.query.get(current_user.id)
    matches = Match.query.filter_by(account_id=current_user.id)
    for match in matches:
        match_comments = Comment.query.filter_by(matchid=match.id)
        for comment in match_comments:
            db.session.delete(comment)
        db.session.delete(match)
    comments = Comment.query.filter_by(account_id=current_user.id)
    for comment in comments:
        db.session.delete(comment)
    logout_user()
    db.session.delete(u)
    db.session.commit()
    flash("User deleted :'(")
    return redirect(url_for("index"))