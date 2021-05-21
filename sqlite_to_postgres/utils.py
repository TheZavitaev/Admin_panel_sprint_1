from psycopg2.extensions import connection as _connection


class PostgresSaver:
    def __init__(self, pg_conn: _connection):
        self.cursor = pg_conn.cursor()
        self._counter = 0