#!/usr/bin/python -B
"""DOCSTRING."""

import MySQLdb
import config


class Database(object):
    """Class to manage connections to MySQL DB."""

    def __init__(self):
        """Main elements of a database connection."""
        self._database = None
        self._cursor = None

        self.make_connection()

    def make_connection(self):
        """Return a connection to the database, (cursor)."""
        try:
            # Make database connection
            self._database = MySQLdb.connect(host=config.HOSTNAME,
                                             user=config.USERNAME,
                                             passwd=config.PASSWORD,
                                             db=config.DATABASE)

            # Obtain cursor for execution
            self._cursor = self._database.cursor()
        except Exception as exception:
            print exception
            return None

    def select_all_from(self, table):
        """Return all rows inside a table."""
        if self._database is None or self._cursor is None:
            return None

        self._cursor.execute('SELECT * FROM {}'.format(table))
        return self._cursor.fetchall()

    def select_from(self, what, table):
        """Return all requested rows inside a table."""
        if self._database is None or self._cursor is None:
            return None

        self._cursor.execute('SELECT {} FROM {}'.format(what, table))
