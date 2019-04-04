from application import db

class Comment(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(250), nullable=False)
    matchid = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    

    def __init__(self, content, matchid):
        self.content = content
        self.matchid = matchid
