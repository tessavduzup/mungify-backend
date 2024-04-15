from application import db


class User(db.Models):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    psw = db.Column(db.String, nullable=True)  # ???
    # КОРЗИНА???

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            # 'psw': self.psw  # ???
        }