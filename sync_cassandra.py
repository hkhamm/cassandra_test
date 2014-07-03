"""
Database Creation Script

Uses Event from models_cassandra to create the keyspace and table in the
Cassandra database. Comparable to Django's syncdb command.
"""

__author__ = "Keith Hamm"
__copyright__ = "Copyright 2014, Analytic Spot"

# cqlengine libs
from cqlengine import connection
from cqlengine.management import sync_table

# cassandra libs
from cassandra.auth import PlainTextAuthProvider

# Local libs
from models_cassandra import Event

# Cassandra details
DATABASE_URLS = ['127.0.0.1', '127.0.0.2' '127.0.0.3']
USERNAME = 'cassandra'
PASSWORD = 'cassandra'

# # Authentication
# auth_provider = PlainTextAuthProvider(username=USERNAME, password=PASSWORD)

# Connecting to the database with authentication
connection.setup(DATABASE_URLS)

sync_table(Event)
