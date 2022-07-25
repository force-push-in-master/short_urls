from contextlib import contextmanager
from typing import Union

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from short_urls.db.models import Base

Session = sessionmaker()
db_engine = None


def init_engine(
    db_name: str,
    user: str,
    pwd: Union[str, None],
    host: str,
    port: int,
    driver: str,
):
    user_pwd = user if not pwd else f'{user}:{pwd}'
    global db_engine
    db_engine = create_engine(f'{driver}://{user_pwd}@{host}:{port}/{db_name}', )
    Base.metadata.bind = db_engine
    Session.configure(bind=db_engine)


@contextmanager
def session_scope():
    global db_engine
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
