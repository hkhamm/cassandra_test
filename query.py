# cqlengine libs
from cqlengine import connection

# Local libs
from models_cassandra import Event

# Cassandra libs
from cassandra.auth import PlainTextAuthProvider

import json

URLS = ['127.0.0.1'] #  ['10.0.1.61', '10.0.1.199', '10.0.1.198'] #
USERNAME = 'cassandra'
PASSWORD = 'cassandra'

# Authentication
auth_provider = PlainTextAuthProvider(username=USERNAME, password=PASSWORD)

# Connecting to the database with authentication
connection.setup(URLS, 'ans', auth_provider=auth_provider)

# Get all objects from the database
# q1 = Event.objects.limit(20000)
q2 = Event.objects.all().limit(10)

# print('q1 size: ' + str(q1.count()))
# print('q2 size: ' + str(q2.count()))

obj = []

for event in q2:
    item = dict(event)
    obj.append(item)

json_obj = json.dumps(str(obj))

print(json.loads(json_obj))
