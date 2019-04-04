from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CommentForm(FlaskForm):
    content = StringField("Comment:", [validators.Length(min=1, max=245)])

    class Meta:
        csrf = False