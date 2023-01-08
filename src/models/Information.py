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
