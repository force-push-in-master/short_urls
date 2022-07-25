from pathlib import Path

import pkg_resources

from short_urls.db.db_engine import init_engine, session_scope
from short_urls.db.parse_db_args import parse_db_args

db_engine = None


def init_db():
    args = parse_db_args()
    init_engine(
        user=args.user,
        host=args.host,
        port=args.port,
        db_name=args.db_name,
        driver=args.driver,
        pwd=args.password,
    )
    with session_scope() as session:
        init_db_sql = Path(pkg_resources.resource_filename('short_urls', 'data/init_db.sql'))
        with open(init_db_sql) as sql:
            session.execute(sql.read())
