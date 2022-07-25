import uvicorn

from short_urls.app import app
from short_urls.db.db_engine import init_engine
from short_urls.db.parse_db_args import parse_db_args


def main():
    args = parse_db_args()
    init_engine(
        user=args.user,
        host=args.host,
        port=args.port,
        db_name=args.db_name,
        driver=args.driver,
        pwd=args.password,
    )

    uvicorn.run(app)
