from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, Integer, Sequence, String

from short_urls.db.models import Base


class Transition(Base):
    __tablename__ = "transition"

    id = Column(Integer, Sequence('transition_id_seq'), primary_key=True)
    code = Column(String, index=True, nullable=False)
    datetime = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
