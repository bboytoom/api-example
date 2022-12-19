import uuid
from src.config.sqlalchemy_db import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'

    uuid = db.Column(
        db.CHAR(36),
        primary_key=True,
        index=True,
        nullable=False,
        default=uuid.uuid4
        )

    email = db.Column(db.String(70), unique=True, index=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    status = db.Column(db.Boolean, default=True)

    created_at = db.Column(
        db.DateTime, nullable=False,
        default=datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        )

    updated_at = db.Column(
        db.DateTime, nullable=False,
        default=datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        )

    def __repr__(self):
        return f'User({self.email}, {self.uuid})'
