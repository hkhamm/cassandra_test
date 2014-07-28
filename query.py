# cqlengine libs
from cqlengine import connection

# Local libs
from models_cassandra import Event

# Cassandra libs
from cassandra.auth import PlainTextAuthProvider

URLS = ['10.0.1.61', '10.0.1.199', '10.0.1.198']
USERNAME = 'cassandra'
PASSWORD = 'cassandra'

# Authentication
auth_provider = PlainTextAuthProvider(username=USERNAME,
                                       password=PASSWORD)

# Connecting to the database with authentication
connection.setup(URLS, 'ans', auth_provider=auth_provider)

# Get all objects from the database
query = Event.objects.filter(event_id='5158669b-fabf-4e44-9d92-c4c157b10f90')
query = query.filter(app_id='app_id0')

# Print all object from the database
for event in query:
    print(dict(event))
