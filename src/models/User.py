import uuid
import logging

from datetime import datetime
from sqlalchemy import and_
from sqlalchemy.orm import load_only
from multipledispatch import dispatch
from werkzeug.security import generate_password_hash, check_password_hash

from src.config.sqlalchemy_db import db

logger = logging.getLogger(__name__)


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = (
        db.Index('ix_users_uuid_email', 'uuid', 'email', unique=True),
        )

    uuid = db.Column(
        db.CHAR(36),
        primary_key=True,
        unique=True,
        index=True,
        nullable=False,
        default=uuid.uuid4
        )

    email = db.Column(db.String(70), unique=True, index=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, index=True, nullable=False)
    image_name = db.Column(db.String(100), nullable=True)
    status = db.Column(db.Boolean, default=True)
    tasks = db.relationship('Task', backref='tasks')
    information = db.relationship(
        'Information',
        cascade='all, delete',
        uselist=False,
        backref='information'
        )

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        )

    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        onupdate=datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"),
        default=datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        )

    def __repr__(self):
        return f'User({self.uuid})'

    @classmethod
    def new_user(cls, _data):
        return User(
            email=_data.get('email'),
            password=generate_password_hash(_data.get('password')),
            first_name=_data.get('first_name'),
            last_name=_data.get('last_name'),
            date_of_birth=_data.get('date_of_birth')
            )

    @dispatch(str)
    def exists_email(_email) -> bool:
        return db.session.query(User.uuid) \
            .filter_by(email=_email) \
            .first() is not None

    @dispatch(str, object)
    def exists_email(_email, _uuid) -> bool:
        return db.session.query(User.uuid) \
            .filter(and_(User.email == _email, User.uuid != _uuid)) \
            .first() is not None

    def verify_password(self, _password):
        return check_password_hash(self.password, _password)

    def retrieve_user(_uuid):
        fields = ['uuid', 'email', 'first_name', 'last_name', 'date_of_birth', 'status']

        return db.session.query(User).filter_by(uuid=_uuid) \
            .options(load_only(*fields)).first()

    def retrieve_all_user():
        fields = ['uuid', 'email', 'first_name', 'last_name', 'date_of_birth', 'status']

        return db.session.query(User) \
            .options(load_only(*fields)).all()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()

            return True
        except Exception as e:
            logger.error(e)

            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            logger.error(e)

            return False
