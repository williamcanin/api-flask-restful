from passlib.hash import sha256_crypt as crypt
from main import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    superuser = db.Column(db.Boolean, default=False, nullable=False)

    @property
    def password_hash(self):
        raise AttributeError("password not readable")

    @password_hash.setter
    def password_hash(self, password):
        self.password = crypt.hash(password)

    def verify_password(self, password):
        if crypt.verify(password, self.password):
            return True
        return False

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self) -> str:
        return f"<User {self.username}>"
