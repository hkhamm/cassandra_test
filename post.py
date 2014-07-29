import logging

# Local libs
from models_cassandra import Event

# cqlengine libs
from cqlengine import connection

# Cassandra libs
from cassandra.auth import PlainTextAuthProvider

URLS = ['10.0.1.61', '10.0.1.199', '10.0.1.198'] # ['127.0.0.1'] # 
USERNAME = 'cassandra'
PASSWORD = 'cassandra'

parameters = {'event_id': '76f1064b-2845-4cdf-871e-f2b6b8033ac9',
	      	  	'lat_long': '27.175015, 78.042155',
              'device_code': '76f1064b-2845-4cdf-871e-f2b6b8033ac9',
              'session_id': '4daa8fca-358b-4963-970f-ed78b37630f5',
              'collection': 'test42',
              'client_timestamp': '2014-06-26 15:03:58-0700',
              'ip_address': '127.0.0.1',
              'api_key': 'secret-ans-8g9xb-key',
              'event_type': 'null',
              'event_timestamp': '2014-06-26 15:03:58-0700',
              'app_id': 'app_id1'}

# Create local variables of parameter elements
event_id = parameters['event_id']

# Required field, no validation required
api_key = parameters['api_key']
app_id = parameters['app_id']
device_code = parameters['device_code']
session_id = parameters['session_id']
event_type = parameters['event_type']

# Convert timestamp strings to datetime objects
event_timestamp = parameters['event_timestamp']
client_timestamp = parameters['client_timestamp']

ip_address = parameters['ip_address']
collection = parameters['collection']
lat_long = parameters['lat_long']

# Create initial assignments for item event columns
correctness = None
item_on_item = None
problem_types = None
item_code = None
item_response = None
difficulty = None
attempts = None

if event_type == 'item':
    # Required
    correctness = parameters['correctness']
    item_on_item = parameters['item_on_item']

    # Not required
    problem_types = parameters['problem_types']
    item_code = parameters['item_code']
    item_response = parameters['item_response']
    difficulty = parameters['difficulty']
    attempts = parameters['attempts']

# TODO generate here?
at_school = '1'
location = 'location 1'

# Check if api_key is valid
#if 'ansApiKey' not in parameters:
#    # todo2: clean up error message, standard json format for response
#    return Response("""{"status":"Missing api_key"}""",
#                    status=status.HTTP_401_UNAUTHORIZED)

#if not is_api_key_valid(api_key):
#    # todo2: clean up error message, standard json format for response
#    return Response("""{"status":"Bad api_key"}""",
#                    status=status.HTTP_401_UNAUTHORIZED)

# todo: validation!?
# cqlengine does model validation in the model class
# https://cqlengine.readthedocs.org/en/latest/topics/models.html

# Debug logging of request parameters
logging.warning(parameters)

# TODO should every post create a new connection?
# TODO catch server connection failure
# TODO if server connection fails return specific status?

# Authentication
auth_provider = PlainTextAuthProvider(username=USERNAME,
                                      password=PASSWORD)

# Connecting to the database with authentication
connection.setup(URLS, 'ans', auth_provider=auth_provider)

if event_type == 'null':
    Event.create(event_id=event_id,
								 api_key=api_key,
                 app_id=app_id,
                 device_code=device_code,
                 session_id=session_id,
                 event_timestamp=event_timestamp,
                 client_timestamp=client_timestamp,
                 event_type=event_type,
                 ip_address=ip_address,
                 collection=collection,
                 lat_long=lat_long,
                 at_school=at_school,
                 location=location)
elif event_type == 'item':
    Event.create(event_id=event_id,
								 api_key=api_key,
                 app_id=app_id,
                 device_code=device_code,
                 session_id=session_id,
                 event_timestamp=event_timestamp,
                 client_timestamp=client_timestamp,
                 event_type=event_type,
                 ip_address=ip_address,
                 collection=collection,
                 lat_long=lat_long,
                 at_school=at_school,
                 location=location,
                 correctness=correctness,
                 item_on_item=item_on_item,
                 problem_types=problem_types,
                 item_code=item_code,
                 item_response=item_response,
                 difficulty=difficulty,
                 attempts=attempts)
