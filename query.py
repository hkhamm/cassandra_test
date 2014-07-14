# cqlengine libs
from cqlengine import connection

# Local libs
from models_cassandra import Event

# Cassandra libs
from cassandra.auth import PlainTextAuthProvider

URLS = ['10.0.1.200', '10.0.1.199', '10.0.1.198']
USERNAME = 'cassandra'
PASSWORD = 'cassandra'

# Authentication
auth_provider = PlainTextAuthProvider(username=USERNAME,
                                       password=PASSWORD)

# Connecting to the database with authentication
connection.setup(URLS, 'ans', auth_provider=auth_provider)

# Get all objects from the database
all_objects = Event.objects.all()

# Print all object from the database
for event in all_objects:
    print(dict(event))
