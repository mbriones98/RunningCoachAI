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

class Activity(BaseModel):
    id: int
    name: str
    distance: float
    athlete: dict

    # optional fields
    moving_time: int | None
    elapsed_time: int | None
    total_elevation_gain: float | None
    type: str | None
    start_date: str | None
    start_date_local: str | None
    timezone: str | None
    average_speed: float | None
    max_speed: float | None
    average_heartrate: float | None
    max_heartrate: float | None
    average_cadence: float | None
    average_temp: float | None
    suffer_score: float | None
    has_heartrate: bool | None
    has_kudoed: bool | None
    workout_type: int | None
    private: bool | None
    device_watts: bool | None
    average_watts: float | None
    max_watts: float | None
    weighted_average_watts: float | None
    kilojoules: float | None
    average_speed: float | None
    max_speed: float | None

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