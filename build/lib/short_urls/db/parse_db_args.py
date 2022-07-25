import argparse


def parse_db_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser('init db args')
    parser.add_argument('--db-name', type=str, required=True)
    parser.add_argument('--driver', type=str, default='postgresql')
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--user', type=str, default='postgres')
    parser.add_argument('--password', type=str, default=None)
    parser.add_argument('--port', type=str, default='5432')

    return parser.parse_args()
