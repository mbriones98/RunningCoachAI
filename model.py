from pydantic import BaseModel
from typing import List

class WebhookEvent(BaseModel):
    object_type: str
    object_id: int
    aspect_type: str
    updates: dict
    owner_id: int
    subscription_id: int
    event_time: int

keepActivityFields = set([
    'id',
    'name',
    'distance',
    'moving_time',
    'elapsed_time',
    'total_elevation_gain',
    'type',
    'start_date',
    'start_date_local',
    'timezone',
    'average_speed',
    'max_speed',
    'average_heartrate',
    'max_heartrate',
    'average_cadence',
    'average_temp',
    'suffer_score',
    'has_heartrate',
    'has_kudoed',
    'workout_type',
    'private',
    'device_watts',
    'average_watts',
    'max_watts',
    'weighted_average_watts',
    'kilojoules',
    'athlete',
    'average_speed',
    'max_speed'
])