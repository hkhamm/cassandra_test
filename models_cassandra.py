"""Database Model"""

__author__ = "Keith Hamm"
__copyright__ = "Copyright 2014, Analytic Spot"

# Std libs
import uuid

# cqlengine libs
from cqlengine import columns
from cqlengine import models


class Event(models.Model):
    """
    Analytic Event
    """
    __keyspace__ = 'ans'
    __table_name__ = 'events'

    # Required General Event Columns

    event_id = columns.UUID(db_field='ansEventId',
                            primary_key=True,
                            default=uuid.uuid4)
    # collected using this api_key
    api_key = columns.Text(db_field='ansApiKey', required=True)
    device_code = columns.UUID(db_field='ansDeviceCode', required=True)
    app_id = columns.Text(db_field='ansApiId', required=True)
    session_id = columns.UUID(db_field='ansSessionId', required=True)

    # Required Item Event Columns

    correctness = columns.Boolean(db_field='ansCorrectness', required=False)
    item_on_item = columns.Float(db_field='ansItemOnItem', required=False)
    # when the item was completed
    event_timestamp = columns.Text(db_field='ansEventTimestamp')
    event_type = columns.Text(db_field='ansEventType', required=True)

    # Other General Events Columns

    ip_address = columns.Text(db_field='ansIpAddress', required=False)
    client_timestamp = columns.Text(db_field='ansClientTimestamp')
    # Name of collection
    collection = columns.Text(db_field='ansCollection', required=False)
    lat_long = columns.Text(db_field='ansLatLong', required=False)

    # Server Generated General Event Columns

    location = columns.Text(db_field='ansLocation', required=False)
    # choices: -1 unknown, 0 no, 1 yes
    at_school = columns.Text(db_field='ansAtSchool', required=False, default=-1)

    # Other Item Event Columns

    # Set or list?
    problem_types = columns.Set(db_field='ansProblemTypes',
                                value_type=columns.Text,
                                required=False)
    item_code = columns.Text(db_field='ansItemCode', required=False)
    item_response = columns.Text(db_field='ansItemResponse', required=False)
    difficulty = columns.Integer(db_field='ansDifficulty', required=False)
    attempts = columns.Integer(db_field='ansAttempts', required=False)


# todo2: will these ITEM properties below become _ans_ prefixed and the library handling it on ios?


# Education specifc event details (store all in flexible json)
# L1 - most important
#   time_on_item - (L1) how long was spent on the item (float in secs, eg: 3.23) [api: float/int/str]
#   first_try_correct (L1) (int 0=no, 1=yes)  [api: int or str]

# L2 less important but helpful
#   item_id (L2 but opt) - anything unique that identifies each question (1+1, 1>2, etc) [api: str]
#   item_difficulty (L2 but opt) - this could be mangled later based on item_id.
#   item_type (opt) - type of item, any unique name to distinguish. only necessary if app has multiple problem types
#   errors_before_correct (opt) - if they get multiple chances to get it correct, how many did it take (0 means they got it right on first try)
#   response_options_count (opt) - if multiple options


# future: Lower Priority
# todo2: country = models.CharField(max_length=2, null=True, blank=True) # two-letter country code
#   item_description - fuller description of the item (e.g. )
#   response_options - actual options for
#   response_value - could be the correct value only or array of each one tried

# FUTURE: Auth only fields
# user_id = models.CharField(max_length=50, null=True, blank=True) # if learner logged in, pushes this as well (in case different learners per device)
# latitude = models.CharField(max_length=50, null=True, blank=True) # future:collapse lat/long into single field?
# longitude = models.CharField(max_length=50, null=True, blank=True)
# ip_address = models.CharField("IP Address", max_length=50, null=True, blank=True) # future: ip-address specific field

# future: handle implications of malfeasance if pushes multiple events with same event_id. what havoc would that cause.
