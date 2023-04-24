import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Text(SqlAlchemyBase):
    __tablename__ = 'text'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    text = sqlalchemy.Column(sqlalchemy.String, nullable=True)
