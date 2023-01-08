import uuid
import enum
import logging

from datetime import datetime
from src.config.sqlalchemy_db import db

logger = logging.getLogger(__name__)


class TypeTasks(enum.Enum):
    no_repeat = 1
    daily = 2


class Task(db.Model):
    __tablename__ = 'tasks'

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
        index=True,
        nullable=False
        )

    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text(), nullable=True)

    type_task = db.Column(
        db.Enum(TypeTasks),
        default=TypeTasks.no_repeat.value,
        index=True,
        nullable=False
        )

    start_data_time = db.Column(
        db.DateTime,
        index=True,
        nullable=False
        )

    end_data_time = db.Column(
        db.DateTime,
        index=True,
        nullable=True
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
        return f'Task({self.uuid}, {self.user_uuid})'
