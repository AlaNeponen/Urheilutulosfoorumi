from flask_wtf import FlaskForm
from wtforms import StringField, validators

class MatchForm(FlaskForm):
    winner = StringField("Winner:", [validators.Length(min=2)])
    opponent = StringField("Opponent:", [validators.Length(min=2)])
    date_when = StringField("Date:(ex. 21 03 2016)", [validators.Length(min=10, max=10)])
    score = StringField("Score:", [validators.Length(min=2)])
    event = StringField("Event:(name of the league, tournament etc.)", [validators.Length(min=2)])


    class Meta:
        csrf = False