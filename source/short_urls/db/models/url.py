from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, String

from short_urls.db.models import Base


class Url(Base):
    __tablename__ = "url"

    code = Column(String, primary_key=True)
    url = Column(String, unique=True, nullable=False, index=True)
    created = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    modified = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
