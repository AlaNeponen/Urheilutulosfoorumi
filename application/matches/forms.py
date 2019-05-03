from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.fields.html5 import DateField

class MatchForm(FlaskForm):
    winner = StringField("Winner:", [validators.Length(min=2)])
    opponent = StringField("Opponent:", [validators.Length(min=2)])
    date_when = DateField("Date:(ex. 21 03 2016)")
    score = StringField("Score:", [validators.Length(min=2)])
    event = StringField("Event:(name of the league, tournament etc.)", [validators.Length(min=2)])


    class Meta:
        csrf = False