from functools import singledispatch

from mara_db import dbs


@singledispatch
def db_jdbc_url(db: object) -> str:
    """Returns a JDBC url for a mara db alias"""
    raise NotImplementedError(f'Please implement jdbc_url for type "{db.__class__.__name__}"')


@db_jdbc_url.register(str)
def __(db: str):
    return db_jdbc_url(dbs.db(db))


@db_jdbc_url.register(dbs.SQLServerDB)
def __(db: dbs.SQLServerDB):
    return (f'jdbc:sqlserver://{db.host}'
            + (f':{db.port}' if db.port else '')
            + (f';user={db.user}' if db.user else ';integratedSecurity=true')
            + (f';password={db.password}' if db.password else '')
            + (f';databaseName={db.database}' if db.database else ''))
