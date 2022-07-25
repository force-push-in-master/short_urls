import setuptools

PACKAGE_NAME = 'short-urls'
DESCRIPTION = 'Short URLs service'
VERSION = '1.0'
AUTHOR = 'Dmitry Sukhov'

def setup():
    setuptools.setup(
        name=PACKAGE_NAME,
        version=VERSION,
        author=AUTHOR,
        description=DESCRIPTION,
        package_data={'': ['data/*']},
        package_dir={'': 'source'},
        packages=setuptools.find_packages(where='source'),
        install_requires=[
            'fastapi',
            'uvicorn',
            'pydantic',
            'sqlalchemy',
            'psycopg2-binary',
        ],
        python_requires='>=3.7',
        entry_points={
            'console_scripts': [
                'short-urls-init-db=short_urls.db.init_db:init_db',
                'short-urls-run=short_urls.main:main',
            ]
        }
    )


if __name__ == '__main__':
    setup()
