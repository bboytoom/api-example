import uuid
import logging

from datetime import datetime
from src.config.sqlalchemy_db import db

logger = logging.getLogger(__name__)


class Information(db.Model):
    __tablename__ = 'information'

    uuid = db.Column(
        db.CHAR(36),
        primary_key=True,
        unique=True,
        index=True,
        nullable=False,
        default=uuid.uuid4
        )

    user_uuid = db.Column(
        db.CHAR(36),
        db.ForeignKey('users.uuid'),
        unique=True,
        index=True,
        nullable=False
        )

    country = db.Column(db.String(50), nullable=True)
    post_code = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=True)
    city = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)

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
        return f'Information({self.uuid}, {self.user_uuid})'

    def exists_user_uuid(_user_uuid):
        return db.session.query(Information.uuid) \
            .filter_by(user_uuid=_user_uuid) \
            .first() is not None

    @classmethod
    def new_user_information(cls, _data):
        return Information(
            user_uuid=_data.get('user_uuid'),
            country=_data.get('country'),
            post_code=_data.get('post_code'),
            state=_data.get('state'),
            city=_data.get('city'),
            address=_data.get('address')
            )

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
