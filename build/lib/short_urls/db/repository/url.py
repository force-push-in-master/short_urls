from typing import Optional
from uuid import uuid4

from sqlalchemy.orm import Session

from short_urls.db.models.url import Url


class UrlRepository:

    @classmethod
    def create_short_url(cls, session: Session, source_url: str) -> str:
        url = cls.get_by_source_url(session, source_url)
        if url:
            return url.code

        code = uuid4().hex[::5]
        url = Url(url=source_url, code=code)
        session.add(url)
        return code

    @classmethod
    def update_source_url(cls, session: Session, code: str, source_url: str) -> None:
        url = cls.get_by_code(session, code)
        url.url = source_url

    @classmethod
    def get_source_url(cls, session: Session, code: str) -> str:
        url = cls.get_by_code(session, code)
        return url.url

    @staticmethod
    def get_by_source_url(session: Session, source_url: str) -> Optional[Url]:
        return session.query(Url).where(Url.url == source_url).first()

    @staticmethod
    def get_by_code(session: Session, code: str) -> Url:
        return session.query(Url).where(Url.code == code).one()

    @classmethod
    def delete_by_code(cls, session: Session, code: str) -> None:
        url = cls.get_by_code(session, code)
        session.delete(url)
