from application import db
from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    matches = db.relationship("Match", backref='account', lazy=True)
    comments = db.relationship("Comment", backref='account', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def most_active_users():
        stmt = text("SELECT Account.username, COUNT(Comment.id) AS numberOfComments FROM Account"
                    " LEFT JOIN Comment ON Comment.account_id = Account.id"
                    " GROUP BY Account.username"
                    " HAVING numberOfComments > 0"
                    " ORDER BY numberOfComments DESC"
                    " LIMIT 3")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "comments":row[1]})

        return response




