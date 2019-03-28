from application import db

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    winner = db.Column(db.String(144), nullable=False)
    opponent = db.Column(db.String(144), nullable=False)
    date_when = db.Column(db.Date)
    score = db.Column(db.String(50), nullable=False)
    event = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    def __init__(self, winner, opponent, date_when, score, event):
        self.winner = winner
        self.opponent = opponent
        self.date_when = date_when
        self.score = score
        self.event = event