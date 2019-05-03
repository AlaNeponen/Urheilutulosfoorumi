from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.fields.html5 import DateField

class MatchForm(FlaskForm):
    winner = StringField("Winner:", [validators.Length(min=2, max=140), validators.Regexp('.*\w+.*')])
    opponent = StringField("Opponent:", [validators.Length(min=2, max=140), validators.Regexp('.*\w+.*')])
    date_when = DateField("Date:(ex. 21 03 2016)")
    score = StringField("Score:", [validators.Length(min=2, max=10), validators.Regexp('.*\w+.*')])
    event = StringField("Event:(name of the league, tournament etc.)", [validators.Length(min=2, max=140), validators.Regexp('.*\w+.*')])


    class Meta:
        csrf = False