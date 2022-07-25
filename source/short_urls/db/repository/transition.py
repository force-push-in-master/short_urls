import datetime
from typing import List

from sqlalchemy.orm import Session

from short_urls.db.models.transition import Transition


class TransitionRepository:

    @staticmethod
    def save_transition(session: Session, code: str) -> None:
        session.add(Transition(code=code))

    @staticmethod
    def get_all(session: Session, code: str) -> List[Transition]:
        return session.query(Transition).where(Transition.code == code).all()

    @staticmethod
    def get_count(session: Session, code: str, only_today: bool = True) -> int:
        query = session.query(Transition).where(Transition.code == code)
        if only_today:
            query = query.where(
                Transition.datetime >= datetime.datetime.combine(
                    datetime.date.today(),
                    datetime.datetime.min.time(),
                )
            )
        return query.count()
